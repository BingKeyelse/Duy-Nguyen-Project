from import_all import*

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Calib.__init__(self)  # Gọi init của Calib

        # Lấy đường dẫn tuyệt đối của file đang chạy 
        self.current_file_path = os.path.dirname(os.path.abspath(__file__))

        # Tạo ra đường dẫn và thư mục hiện thời để lưu cho NG
        self.auto_check_and_create_folder_and_file_NG()
        
        # Tạo data SQLite
        self.creat_or_check_database()

        # cập nhập time và date sau 1s
        self.timer_date = QTimer(self)
        self.timer_date.timeout.connect(self.monitor_month_change)
        self.timer_date.start(60000)  # Update after 60s

        # Khởi động setup liên quan đết giao diện ban đầu
        self.initial_UI_setup()
        # Lấy giá trị cho việc sử dụng cho calib ảnh
        json_path = os.path.join(self.current_file_path, "data_calib", "calib_camera.json")

        self.frame_calibrate = FrameCalibrate(json_path)
        
        # Liên kết widget khi thay đổi với label để thể hiện ảnh không bị sai lệch
        self.ui.stackedWidget.currentChanged.connect(self.on_page_changed)

        ##### Cam 1
        # Khởi tạo queue với camera 1
        self.current_queue_cam1 = queue.Queue(maxsize=1)
        self.mode_pic_cam1= Value("i",0)  # 0: Cam 1, 1: Calib, 2: Sample
        self.image_sample_cam1=cv2.imread(os.path.join(self.current_file_path, "picture", "saved_sample.png"))

        


        # Khai báo biến
        # H high, S high, V high, H low, S low, V low, bright, contrast, ratio, R cirrcle
        self.value_saved_cam1=[None, None, None, None, None, None, None, None, None, None] 
        self.value_now_cam1=[None, None, None, None, None, None, None, None, None, None] 
        self.image_cam1=None

        

        Cam_1.start(self)
        Cam_1.slider_change_value_cam1(self)

        self.slider_timer = QTimer()
        self.slider_timer.setSingleShot(True)
        self.slider_timer.timeout.connect(lambda: self.process_cam_1(self.value_now_cam1))

        self.ui.but_saving_cam1.clicked.connect(lambda: Cam_1.save_data(self))
        self.ui.but_undo_cam1.clicked.connect(lambda: Cam_1.undo_data(self))
        self.ui.but_take_picture_cam1.clicked.connect(self.trigger_cam_1)
        self.ui.but_result_cam1.clicked.connect(lambda: Cam_1.switch_page(self))
        self.center_cam1=0



        # ✅ Khởi tạo camera Basler
        self.camera = camera_Basler_multi(self.current_queue_cam1,self.mode_pic_cam1) # Chỉ có calib là gửi số 0 đi
        self.camera.begin()





        #### Calib
        # Chức năng của Calib
        Calib.start(self) # khởi động ban đầu mà không cần phải init
        self.ui.but_clear_calib.clicked.connect(lambda: Calib.clear_file_image(self))
        self.ui.but_take_calib.clicked.connect(self.trigger_cam_calib)
        self.ui.but_calib_calib.clicked.connect(self.auto_calib)
        
        ### Sample
        self.sample=Sample(self)
        self.ui.but_take_sample.clicked.connect(self.trigger_cam_sample)


        #### Hàm setup chức năng cho UI như nút nhấn, chuyển giao diện
        UI_of_main_gui.update_ram_and_disk_time_and_date(self)
        UI_of_main_gui.change_window(self)
        UI_of_main_gui.tranfer_window(self)


        # Các hàm threading
        thread1= threading.Thread(target=self.process_queue_cam1, daemon=True)
        thread1.start()

    def check(self):
        print(f'OKOKOKOKOK: {self.value_now_cam1}')

    def read_file(self, link):
        data_read= open(link,"r")
        data=data_read.readlines()
        data_read.close()
        return data
    
    def exchange_data(self,data):
        processed = []
        for i, value in enumerate(data):
            try:
                if i == 7 :  # Phần tử thứ 5 và 6 (index 4 và 5) -> float
                    processed.append(float(value))
                else:  # Các phần tử khác -> int
                    processed.append(int(value))
            except ValueError:
                processed.append(value)  # Nếu không chuyển được, giữ nguyên
        return processed


    def on_page_changed(self, index):
        """Cập nhật ảnh khi trang có QLabel xuất hiện"""
        if self.ui.stackedWidget.currentWidget() == self.ui.window_1:
            self.mode_pic_cam1.value=0
        elif self.ui.stackedWidget.currentWidget() == self.ui.window_2:
            QTimer.singleShot(50, lambda: Calib.check_file_in_folder(self))
            self.mode_pic_cam1.value=1
        elif self.ui.stackedWidget.currentWidget() == self.ui.window_3:
            self.mode_pic_cam1.value=2
        
    def initial_UI_setup(self):
        ## Đóng màn hình full icon
        self.ui.window_expand.hide()

        # Setup màn Cam 1
        self.ui.show_pic_cam_cam1.setFixedSize(419, 428)
        self.ui.show_pic_thread_cam1.setFixedSize(419, 428)
        self.ui.show_pic_real_cam1.setFixedSize(419, 428)
        self.ui.show_pic_virtual_cam1.setFixedSize(419, 428)


        # Tạo QLabel mới trên nền của màn hình hiện ảnh của calib
        self.current_label = QLabel("          ", self.ui.show_pic_calib_calib)
        self.current_label.setStyleSheet("color: black; font-size: 16px;")

        self.ui.show_pic_calib_calib.setFixedSize(495, 492)

        # Setup màn Sample
        self.ui.show_pic_real_sample.setFixedSize(426, 508)
        self.ui.show_pic_sample_sample.setFixedSize(426, 508)

    def trigger_cam_1(self):
        self.mode_pic_cam1.value=0
        self.camera.trigger_cam()
     

    def trigger_cam_sample(self):
        self.mode_pic_cam1.value=2
        self.camera.trigger_cam()


    def trigger_cam_calib(self):
        if self.file_count_calib <7: # Khi khởi tạo calib thì biết này 
            #mình tự động lấy được, thông qua hàm start
            self.mode_pic_cam1.value=1 # 

            """Gọi trigger để chụp ảnh"""
            self.camera.trigger_cam()
        # Calib.check_file_in_folder(self)
        

    def process_queue_cam1(self):
        while True:
            if not self.current_queue_cam1.empty():
                image= self.current_queue_cam1.get()
                if self.mode_pic_cam1.value==1 and self.file_count_calib <7:
                    image_path = os.path.join(self.current_file_path, "data_calib", f"{self.file_count_calib+1}.png")
                    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    cv2.imwrite(image_path,image)
                    Calib.check_file_in_folder(self)

                elif self.mode_pic_cam1.value==2:
                    # Qua lớp calib
                    image = self.frame_calibrate.undistortImage(image.copy()) 
                    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


                    link = os.path.join(self.current_file_path, "picture", "sample_cam1.png")
                    cv2.imwrite(link,image)

                    self.sample.reset()

                else:
                    # Qua lớp calib
                    image = self.frame_calibrate.undistortImage(image.copy())
                    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                    # link = os.path.join(self.current_file_path, "picture", "test_cam1.png")
                    # cv2.imwrite(link,image)

                    self.image_cam1=image.copy()

                    self.image_sample_cam1=cv2.imread(os.path.join(self.current_file_path, "picture", "saved_sample.png"))

                    # Temp-matching hình ảnh nguyên bản được vẽ lên và hình ảnh nhỏ của vùng được scale
                    self.image_process, self.image_matching_process=self.template_matching(self.image_cam1.copy(),self.image_sample_cam1.copy())
                    if self.image_matching_process is not None:
                        cv2.imwrite(r'picture\real_circle_canny.png', self.image_matching_process)
                    if self.image_process is not None and self.image_matching_process is not None:

                        UI_of_main_gui.show_image_3chanel(self,self.image_process,self.ui.show_pic_cam_cam1)
                    else: 
                        UI_of_main_gui.show_image_3chanel(self,self.image_cam1,self.ui.show_pic_cam_cam1)


                    self.process_cam_1(self.value_saved_cam1)
                    

    def process_cam_1(self, value):

        if self.image_process is not None and self.image_matching_process is not None:
            # Hình ảnh cắt ra của hình chữ nhật đó
            image_matching_process_drawed=self.image_matching_process.copy()
            picture_drawed=0

            contours=0

            image_process=cv2.convertScaleAbs(self.image_matching_process.copy(), alpha = value[7], beta = value[6])
            hsv = cv2.cvtColor(image_process.copy(), cv2.COLOR_BGR2HSV)

            # # Tạo mask bằng cách phân ngưỡng
            upper_hsv= value[0],value[1], value[2]
            lower_hsv= value[3],value[4], value[5]
        
            mask = cv2.inRange(hsv, (lower_hsv), (upper_hsv))
            mask = cv2.bitwise_not(mask)

            # Tìm contours
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
          
            if contours:
                # Tìm contour lớn nhất
                largest_contour = max(contours, key=cv2.contourArea)

                # Vẽ bounding box thẳng
                x, y, w, h = cv2.boundingRect(largest_contour)
                padding = 15
                y1, y2 = max(0, y - padding), min(mask.shape[0], y + h + padding)
                x1, x2 = max(0, x - padding), min(mask.shape[1], x + w + padding)
                # cropped_image = mask[y:y+h, x:x+w]
                # Cắt ảnh với vùng mở rộng
                cropped_image = mask[y1:y2, x1:x2]
                # cv2.imwrite(r"picture\test_circle.png", cropped_image)
                picture_drawed=image_matching_process_drawed[y1:y2, x1:x2]

                image_insert= self.check_bavia(picture_drawed, cropped_image, value)
                # print(cropped_image.shape)

                image_matching_process_drawed[y1:y2, x1:x2]=image_insert

                cv2.rectangle(image_matching_process_drawed, (x, y), (x + w, y + h), (0, 0, 255), 2)

            
                # UI_of_main_gui.show_image_3chanel(self,self.image_process,self.ui.show_pic_cam_cam1)
            
            UI_of_main_gui.show_image_3chanel(self,image_matching_process_drawed,self.ui.show_pic_real_cam1)
            UI_of_main_gui.show_image_3chanel(self,mask,self.ui.show_pic_thread_cam1)

        else:
            UI_of_main_gui.show_image_3chanel(self,self.image_cam1.copy(),self.ui.show_pic_cam_cam1)
            self.ui.show_pic_real_cam1.clear()
            self.ui.show_pic_thread_cam1.clear()

    def check_bavia(self,image , image_gray, value):
        # Tìm contour lớn nhất (hình tròn)
        contours, _ = cv2.findContours(image_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            print("Không tìm thấy hình tròn trong ảnh.")
            return None
    
        largest_contour = max(contours, key=cv2.contourArea)

        # Xác định tâm bằng bounding box của contour
        x, y, w, h = cv2.boundingRect(largest_contour)
        cx, cy = int(x + w / 2), int(y + h / 2)  # Tâm của bounding box

        # Tạo mask từ contour
        mask = np.zeros_like(image_gray.copy())
        cv2.drawContours(mask, [largest_contour], -1, 255, thickness=1)

        # Tạo ảnh màu để vẽ kết quả
        output_virtual = cv2.cvtColor(mask.copy(), cv2.COLOR_GRAY2BGR)

        # 🔹 **BƯỚC 1: Tạo bảng góc trước**
        angles_ref = np.linspace(0, 360, 360, endpoint=False)  # 360 giá trị từ 0° đến 359°

        # 🔹 **BƯỚC 2: Tính toán nhanh góc & khoảng cách**
        contour_points = largest_contour[:, 0, :]  # Lấy danh sách các điểm biên

        # Tính khoảng cách từ tâm đến từng điểm biên
        dx = contour_points[:, 0] - cx
        dy = contour_points[:, 1] - cy
        distances = np.sqrt(dx**2 + dy**2)

        # Tính góc của từng điểm so với tâm
        angles = np.arctan2(dy, dx) * 180 / np.pi  # Chuyển đổi sang độ
        angles = np.mod(angles, 360)  # Đảm bảo góc trong khoảng 0-360

        # 🔹 **BƯỚC 3: Ánh xạ khoảng cách vào mảng `r_list`**
        r_list = np.full(360, np.nan)

        # Tìm góc gần nhất trong `angles_ref` bằng broadcasting
        angle_indices = np.abs(angles[:, None] - angles_ref).argmin(axis=1)

        # Gán khoảng cách vào r_list
        for i in range(len(angle_indices)):
            r_list[angle_indices[i]] = distances[i]

        # **Nội suy giá trị NaN để làm mượt**
        valid_r = r_list[~np.isnan(r_list)]  # Lọc bỏ giá trị NaN

        # Kiểm tra nếu valid_r rỗng
        if valid_r.size == 0:
            print("⚠️ Không có giá trị hợp lệ trong r_list! Đặt mặc định r = 0")
            valid_r = np.array([0])  # Tránh lỗi khi tính mean

        for i in range(len(r_list)):
            if np.isnan(r_list[i]):
                start_idx = max(0, i - 5)
                end_idx = min(len(valid_r), i + 5)

                # Nếu đoạn cần lấy trung bình vẫn rỗng, thì thay thế bằng giá trị mặc định
                if valid_r[start_idx:end_idx].size == 0:
                    r_list[i] = 0  # Giá trị mặc định khi không có dữ liệu hợp lệ
                else:
                    r_list[i] = np.mean(valid_r[start_idx:end_idx])  # Trung bình cục bộ

        # **Tính bán kính trung bình từ 100 giá trị nhỏ nhất**
        first_120 = np.random.choice(valid_r[:80], min(25, len(valid_r[:80])), replace=False)  # Lấy ngẫu nhiên 50 giá trị từ giữa
        middle_50 = np.random.choice(valid_r[80:300], min(120, len(valid_r[80:300])), replace=False)  # Lấy ngẫu nhiên 50 giá trị từ giữa
        last_10 = np.random.choice(valid_r[300:], min(10, len(valid_r[300:])), replace=False)  # Lấy ngẫu nhiên 50 giá trị từ giữa

        # Gộp tất cả vào một danh sách
        selected_values = np.concatenate([ middle_50,last_10])

        # Tính r_mean
        r_mean = np.median(np.sort(selected_values))

        # Debug số lượng góc có giá trị hợp lệ
        # print(f"Số góc có giá trị hợp lệ: {np.count_nonzero(~np.isnan(r_list))} / 360")

        # Nội suy nếu còn thiếu
        valid_indices = np.where(~np.isnan(r_list))[0]
        valid_r_values = r_list[valid_indices]
        full_indices = np.arange(360)
        r_list = np.interp(full_indices, valid_indices, valid_r_values)

        # **Vẽ các đường tia**
        count_red = 0
        for angle in range(0, 360, 2):  # Giảm mật độ tia (mỗi 5 độ)
            theta = np.deg2rad(angle)
            r = r_list[angle]

            # Xác định màu sắc
            if value[9]< abs(r - r_mean):
                color = (0, 0, 255)  # Đỏ nếu bất thường
                count_red += 1  
            else:
                color = (0, 255, 0)  # Xanh nếu ổn

            # Xác định điểm kết thúc
            x_end, y_end = int(cx + r * np.cos(theta)), int(cy + r * np.sin(theta))

            # Vẽ đường tia
            cv2.line(output_virtual, (cx, cy), (x_end, y_end), color, 1)
            if color==(0, 0, 255):
                cv2.line(image, (cx, cy), (x_end, y_end), color, 1)

        self.ui.show_value_now_cam1.setText(f'Điểm NG phát hiện: {count_red}')

        if count_red > value[8]:
            self.ui.label_ok_cam1.setStyleSheet(f"background: #47ff4d;")
            self.ui.label_ng_cam1.setStyleSheet(f"background: #c6c6c6;")
        else:
            self.ui.label_ok_cam1.setStyleSheet(f"background: #c6c6c6;")
            self.ui.label_ng_cam1.setStyleSheet(f"background: #ff0772;")

        
        UI_of_main_gui.show_image_3chanel(self,output_virtual,self.ui.show_pic_virtual_cam1)


        return image


    def template_matching(self, image, sample):
        image_draw=None
        matched_region=None

        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)

        # Tạo mask để loại bỏ nền đen
        _, mask = cv2.threshold(gray_template, 10, 255, cv2.THRESH_BINARY)

        # Matching sử dụng template matching
        result = cv2.matchTemplate(gray_img, gray_template, cv2.TM_CCOEFF_NORMED, mask=mask)

        # Tìm vị trí matching tốt nhất
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # Kiểm tra nếu matching trên 80%
        threshold = 0.75  # Ngưỡng tối thiểu 80%
        print(f'Ngưỡng hiện tại: {max_val}')
        if max_val >= threshold:
            # Vẽ hình chữ nhật quanh vùng matching
            h, w = gray_template.shape
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            image_draw=image.copy()
            cv2.rectangle(image_draw, top_left, bottom_right, (0, 255, 0), 2)

            # Cắt ảnh vùng matching
            matched_region = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        
        # center_x = (top_left[0] + bottom_right[0]) // 2
        # center_y = (top_left[1] + bottom_right[1]) // 2
        # self.center_cam1=(center_x,center_y)

        return image_draw, matched_region

            



                    

    def auto_calib(self):
        if self.file_count_calib>=5:
            json_path = os.path.join(self.current_file_path, "data_calib", "calib_camera.json")

            path_folder = os.path.join(self.current_file_path, "data_calib")
            bmp_files = os.path.join(path_folder, "*.png")  # Lấy tất cả file bmp

            self.frame_calibrate = FrameCalibrate(json_path)

            image,ret= self.frame_calibrate.calibrateCameraMatrix(
            bmp_files, 
            (23, 15), 
            5, True)
            if ret !=0:
                UI_of_main_gui.show_image_3chanel(self, image, self.ui.show_pic_calib_calib)
                self.current_label.setStyleSheet(f"background-color: green;")

            else:
                self.current_label.setText(f"Không calib được")
                self.current_label.setStyleSheet(f"background-color: red;")

    def save_change_into_database(self,link_database , file_path, name):
        """Lưu ảnh vào database nếu chưa tồn tại."""
        saved_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Mở kết nối mới
        conn = sqlite3.connect(link_database)
        cursor = conn.cursor()


        try:
            cursor.execute("INSERT INTO images (filename, filepath, saved_at) VALUES (?, ?, ?)", 
                        (name, file_path, saved_at))
            conn.commit()
            print(f"✅ Đã lưu: {name}")
        except sqlite3.IntegrityError:
            print(f"⚠️ Đã tồn tại: {name}")
    
    def creat_or_check_database(self):
        self.database_cam1= os.path.join(self.current_file_path,'data_txt', 'database_cam1')

        # Kiểm tra và kết nối tồn tại hoặc tạo mới
        self.conn_cam1 = sqlite3.connect(self.database_cam1)
        self.cursor_cam1 = self.conn_cam1.cursor()
    
            # Tạo bảng lưu ảnh nếu chưa tồn tại
        self.cursor_cam1.execute('''
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT UNIQUE,
                filepath TEXT,
                saved_at TEXT
            )
        ''')
        self.conn_cam1.commit()

    def auto_check_and_create_folder_and_file_NG(self):
        link=os.path.join(self.current_file_path, "data_NG")

        self.year_backup=[]
        self.month_backup=[]
        self.path_ng_save_today=None

        today=datetime.today()
        # Lấy thời điểm hiện tại
        self.month_now=today.month
        self.year_now=today.year

        # Tao folder hien tai de su dung cho muc dich luu tru
        self.path_folder_year_now   = os.path.join(link,str(self.year_now))
        self.path_folder_today_ng_now_cam1   = os.path.join(self.path_folder_year_now ,str(self.month_now),'cam1')
        ## Nếu không có thì phải tạo
        if not os.path.exists(self.path_folder_today_ng_now_cam1):
            os.makedirs(self.path_folder_today_ng_now_cam1)

        # check lai folder voi muc dich chi co the chua duoc nhieu nhat 6 thang

        # check năm
        for year in os.listdir(link):
            self.year_backup.append(year)
        self.year_backup=sorted(self.year_backup)
        check_year_now=os.path.join(link, self.year_backup[-1])

        # Check tháng trong năm nhỏ nhất trong chuỗi
        for month in os.listdir(check_year_now):
            self.month_backup.append(month)
        self.month_backup=sorted(self.month_backup)

        if int(self.month_backup[-1])>=6:
            if len(self.month_backup)>6:
                for month in self.month_backup[0:-6]:
                    path_month_clear=os.path.join(check_year_now,month)

                    if os.path.exists(path_month_clear):
                        shutil.rmtree(path_month_clear)
            
            for year in self.year_backup[:-1]:
                path_year_to_clear=os.path.join(link, year)

                if os.path.exists(path_year_to_clear):
                    shutil.rmtree(path_year_to_clear)
        else:
            # số tháng còn có thể chứa lại bên kia là 
            month_cap=6-int(self.month_backup[-1])
            if len(self.year_backup) >= 2:
                path_year_old=os.path.join(link, self.year_backup[-2])
                for month in os.listdir(path_year_old):
                    # month=month
                    if int(month)<=(12-month_cap):
                        path_month_old_clear=os.path.join(path_year_old,month)
                        if os.path.exists(path_month_old_clear):
                            shutil.rmtree(path_month_old_clear)

    
    def monitor_month_change(self):
        current_month = datetime.now().month

        if current_month != self.month_now:  # Nếu tháng thay đổi
            self.auto_check_and_create_folder_and_file_NG()

    def closeEvent(self, event):
        print("Ngắt kết nối camera thoát chương trình")
        self.camera.close()
        event.accept()

class camera_Basler_multi:
    def __init__(self, pic_queue, mode):
        """Khởi tạo class camera"""
        self.pic_queue = pic_queue
        self.mode=mode

        self.cam = None
        self.converter = None
        self.running = True  # Biến kiểm soát vòng lặp thread trigger
        self.trigger_thread = None 


    def begin(self):
        """Mở camera và bắt đầu chụp"""
        try:
            # ✅ Khởi tạo camera
            tlFactory = pylon.TlFactory.GetInstance()
            devices = tlFactory.EnumerateDevices()

            if len(devices) == 0:
                raise RuntimeError("🚨 Không tìm thấy camera!")

            self.cam = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            self.cam.Open()
            self.cam.StopGrabbing()
            self.cam.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

            # ✅ Cấu hình trigger phần cứng
            self.cam.LineSelector.SetValue('Line1')  
            self.cam.LineMode.SetValue('Input')
            # print(f"📡 Trigger Mode: {self.cam.TriggerMode.GetValue()}")
            # self.cam.TriggerMode.SetValue("On")


            # ✅ Cấu hình converter cho ảnh
            self.converter = pylon.ImageFormatConverter()
            self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
            self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

            print("✅ Camera đã sẵn sàng!")

            # ✅ Bắt đầu theo dõi tín hiệu trigger phần cứng
            self.trigger_thread = self.monitor_trigger()
            self.trigger_thread.start()

        except Exception as e:
            print(f"❌ Lỗi khởi tạo camera: {e}")
    
    def monitor_trigger(self):
        def run():
            """Luồng chạy liên tục kiểm tra tín hiệu từ Line1"""
            previous_status = 0  # Trạng thái trước đó của Line1
            while self.running:
                try:
                    line_status = self.cam.LineStatus.GetValue()
                    if line_status == 1 and previous_status == 0:  # Chỉ chụp khi có sự thay đổi từ 0 → 1
                        print("🎯 Tín hiệu kích hoạt! Chụp ảnh...")
                        self.trigger_cam()

                    previous_status = line_status  # Cập nhật trạng thái
                    time.sleep(0.005)  # Tránh tiêu tốn CPU quá nhiều
                except Exception as e:
                    print(f"❌ Lỗi khi theo dõi trigger: {e}")
        return  threading.Thread(target=run, daemon=True)

    def trigger_cam(self):
        """Chụp ảnh từ camera"""
        if self.cam is None or not self.cam.IsGrabbing():
            print("⚠ Camera chưa sẵn sàng!")
            return

        try:
            grab_result = self.cam.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grab_result.GrabSucceeded():
                img = self.converter.Convert(grab_result).GetArray()
                image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # ✅ Kiểm tra trước khi đưa ảnh vào queue
                if not self.pic_queue.full():
                    self.pic_queue.put(image)
                    print("📸 Ảnh đã được gửi về GUI!")

        except Exception as e:
            print(f"❌ Lỗi chụp ảnh: {e}")

    def close(self):
        self.running=False
        if self.trigger_thread is not None:
            self.trigger_thread.join()
        """Dừng camera"""
        if self.cam is not None:
            self.cam.StopGrabbing()
            self.cam.Close()
        
        print("✅ Camera đã được đóng an toàn.")

#class_calib_images
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
    
class FrameCalibrate:

    CAMERA_MATRIX = 'Camera matrix'
    OPPT_CAMERA_MATRIX = 'Optimal camera matrix'
    DISTORT_ROI = 'Distortion ROI'
    DISTORTION = 'Distortion'
    FRAME_SIZE = 'Frame size'

    # Camera calibration matrix
    camera_matrix = []
    optimal_camera_matrix = []
    distort_roi = []
    camera_dist = []
    homo_matrix = []
    frame_size = (0, 0)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    def __init__(self, config_path):
        self.cfg_file_path = str(config_path)
        self.camera_matrix = self.loadMatrix(self.CAMERA_MATRIX)
        self.camera_dist = self.loadMatrix(self.DISTORTION)
        self.frame_size = self.loadMatrix(self.FRAME_SIZE)
        self.optimal_camera_matrix = self.loadMatrix(self.OPPT_CAMERA_MATRIX)
        self.distort_roi = self.loadMatrix(self.DISTORT_ROI)

    def loadMatrix(self, key):
        obj_text = codecs.open(self.cfg_file_path, 'r', encoding='utf-8').read()
        json_load  = json.loads(obj_text)
        value = json_load.get(key)
        if value is not None:
            matrix_restored = np.asarray(json_load[key])
        else:
            matrix_restored = []
        return matrix_restored

    def saveMatrix(self, key, value):
        print(key)
        print(value)
        obj_text = codecs.open(self.cfg_file_path, 'r', encoding='utf-8').read()
        json_load  = json.loads(obj_text)
        json_load[key] = np.asarray(value)
        json.dump(json_load, 
                    (codecs.open(self.cfg_file_path, 'w', encoding='utf-8')), 
                    indent=4, 
                    cls=NumpyEncoder)

    def calibrateCameraMatrix(self, input_images_path, grid_size, distance, use_chess_board = True):

        grid_points = np.zeros((grid_size[0] * grid_size[1], 3), np.float32)
        grid_points[:,:2] = np.mgrid[0:grid_size[0],0:grid_size[1]].T.reshape(-1,2)
        grid_points = grid_points * distance

        object_points = []
        image_points = []
        input_images = glob.glob(input_images_path)

        for counter in range(len(input_images)):
            # image = mpimg.imread(input_images[counter], )
            image = cv2.imread(input_images[counter], cv2.IMREAD_GRAYSCALE)

            
            if (len(image.shape) == 2) :
                gray_image = image
            else :
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            if counter == 0:
                self.frame_size = gray_image.shape[::-1]
                # print(self.frame_size)
                # print(gray_image.shape[::-1])

            if use_chess_board:
                ret, corners = cv2.findChessboardCorners(image, grid_size, None)
            else:
                ret, corners = cv2.findCirclesGrid(image, grid_size, None)

            if ret == True:

                object_points.append(grid_points)
                corners2 = cv2.cornerSubPix(image, corners, (11,11), (-1,-1), self.criteria)
                image_points.append(corners)

                # color_image = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
                image_copy = image.copy()
                color_image = cv2.cvtColor(image_copy, cv2.COLOR_GRAY2BGR)
                cv2.drawChessboardCorners(color_image, grid_size, corners2, ret)
                # save_path = result_images_path.replace('*', str(counter))
                # cv2.imwrite(save_path, image_copy)

            counter += 1
        try:
            ret, self.camera_matrix, self.camera_dist, rvecs, tvecs =  cv2.calibrateCamera(
                                                                        object_points, 
                                                                        image_points, 
                                                                        self.frame_size, 
                                                                        None, None)

            self.optimal_camera_matrix, self.distort_roi = cv2.getOptimalNewCameraMatrix(
                                                    self.camera_matrix,
                                                    self.camera_dist,
                                                    self.frame_size, 1, 
                                                    self.frame_size)

            self.saveMatrix(self.CAMERA_MATRIX, self.camera_matrix)
            self.saveMatrix(self.DISTORTION, self.camera_dist)
            self.saveMatrix(self.FRAME_SIZE, self.frame_size)
            self.saveMatrix(self.OPPT_CAMERA_MATRIX, self.optimal_camera_matrix)
            self.saveMatrix(self.DISTORT_ROI, self.distort_roi)
            return color_image,ret
        except Exception as e:
            print(f"❌ Lỗi calibration: {e}")
            return None,0
        
    def undistortImage(self, image):
        image_undistort = cv2.undistort(image, self.camera_matrix, 
                                        self.camera_dist, None, self.optimal_camera_matrix)

        x, y, w, h = self.distort_roi
        image_undistort = image_undistort[y:y+h, x:x+w]
        return image_undistort

    

if __name__ == "__main__":
    ### Convert 
    # auto_tranfer_file.convert_ui_qrc_to_py()
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

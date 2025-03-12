from import_all import*

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Lấy đường dẫn tuyệt đối của file đang chạy 
        self.current_file_path = os.path.dirname(os.path.abspath(__file__))


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

        # Khai báo biến
        # H high, S high, V high, H low, S low, V low, bright, contrast, ratio
        self.value_saved_cam1=[None, None, None, None, None, None, None, None, None] 
        self.value_now_cam1=[None, None, None, None, None, None, None, None, None] 
        Cam_1.start(self)
        Cam_1.slider_change_value_cam1(self)
        # self.ui.but_saving_cam1.clicked.connect(lambda: Cam_1.save_data(self))
        self.ui.but_saving_cam1.clicked.connect(self.check)
        self.ui.but_undo_cam1.clicked.connect(lambda: Cam_1.undo_data(self))


        # ✅ Khởi tạo camera Basler
        self.camera = camera_Basler_multi(self.current_queue_cam1,self.mode_pic_cam1) # Chỉ có calib là gửi số 0 đi
        self.camera.begin()


        #### Calib
        # Chức năng của Calib
        Calib.start(self) # khởi động ban đầu mà không cần phải init
        self.ui.but_clear_calib.clicked.connect(lambda: Calib.clear_file_image(self))
        self.ui.but_take_calib.clicked.connect(self.trigger_cam_calib)
        self.ui.but_calib_calib.clicked.connect(self.auto_calib)
        
        

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
        if self.ui.stackedWidget.currentWidget() == self.ui.window_2:
            QTimer.singleShot(50, lambda: Calib.check_file_in_folder(self))


    def initial_UI_setup(self):
        ## Đóng màn hình full icon
        self.ui.window_expand.hide()

        # Tạo QLabel mới trên nền của màn hình hiện ảnh của calib
        self.current_label = QLabel("          ", self.ui.show_pic_calib_calib)
        self.current_label.setStyleSheet("color: black; font-size: 16px;")

        self.ui.show_pic_calib_calib.setFixedSize(495, 492)
        # self.ui.widget_2.layout().setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

    def trigger_cam_calib(self):
        if self.file_count_calib <7: # Khi khởi tạo calib thì biết này 
            #mình tự động lấy được, thông qua hàm start
            self.mode_pic_cam1.value=1 # quy định giá trị là 0 thì không có calib ảnh

            """Gọi trigger để chụp ảnh"""
            self.camera.trigger_cam()
        Calib.check_file_in_folder(self)
        

    def process_queue_cam1(self):
        while True:
            if not self.current_queue_cam1.empty():
                image= self.current_queue_cam1.get()
                if self.mode_pic_cam1.value==1:
                    image_path = os.path.join(self.current_file_path, "data_calib", f"{self.file_count_calib+1}.png")
                    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    cv2.imwrite(image_path,image)
                    Calib.check_file_in_folder(self)
                    

    def auto_calib(self):
        if self.file_count_calib>=5:
            json_path = os.path.join(self.current_file_path, "data_calib", "calib_camera.json")

            path_folder = os.path.join(self.current_file_path, "data_calib")
            bmp_files = os.path.join(path_folder, "*.png")  # Lấy tất cả file bmp

            self.frame_calibrate = FrameCalibrate(json_path)

            image,ret= self.frame_calibrate.calibrateCameraMatrix(
            bmp_files, 
            (19, 16), 
            10, True)
            if ret !=0:
                UI_of_main_gui.show_image_3chanel(self, image, self.ui.show_pic_calib_calib)
                self.current_label.setStyleSheet(f"background-color: green;")

            else:
                self.current_label.setText(f"Không calib được")
                self.current_label.setStyleSheet(f"background-color: red;")

            




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
            self.cam.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

            # ✅ Cấu hình trigger phần cứng
            self.cam.LineSelector.SetValue('Line1')  
            self.cam.LineMode.SetValue('Input')

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

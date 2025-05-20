from import_all import*

class Sample():
    def __init__(self, parent: "MainWindow"):
        self.parent = parent
        # Lấy đường dẫn tuyệt đối của file đang chạy 
        self.current_file_path = os.path.dirname(os.path.abspath(__file__))
        self.sample_path = os.path.join(self.current_file_path, "picture", "sample_cam1.png")

        self.masked_image=None

        # Đọc ảnh gốc
        self.image_original_sample = cv2.imread(self.sample_path)
        self.image_original_sample = cv2.cvtColor(self.image_original_sample, cv2.COLOR_BGR2RGB)

        self.image = self.image_original_sample.copy()  # Sao chép ảnh để vẽ mà không làm mất ảnh gốc

        self.center_sample = None
        self.radius_sample = 0
        self.dragging_sample = False  # Trạng thái kéo hình tròn

        self.temporary_sample= []
        self.point_circle_back_path = os.path.join(self.current_file_path, "data_txt", "point_circle_sample.txt")
        self.data_sample= self.read_value_file_back(self.point_circle_back_path)

        # Gán ảnh lên QLabel
        self.display_image(self.image, self.parent.ui.show_pic_real_sample)
        # UI_of_main_gui.show_image_3chanel(self,self.image, self.parent.ui.show_pic_real_sample)

        # Sự kiện chuột
        self.parent.ui.show_pic_real_sample.mousePressEvent = self.mouse_press_event
        self.parent.ui.show_pic_real_sample.mouseMoveEvent = self.mouse_move_event
        self.parent.ui.show_pic_real_sample.mouseReleaseEvent = self.mouse_release_event

        self.parent.ui.but_sample_sample.clicked.connect(self.function_button_take_sample)
        self.parent.ui.but_clear_sample.clicked.connect(self.function_button_clear_sample)
    
    def reset(self):
        """Cập nhật ảnh mới và vẽ lại nếu có hình tròn"""
        self.image_original_sample = cv2.imread(self.sample_path)
        self.image_original_sample = cv2.cvtColor(self.image_original_sample, cv2.COLOR_BGR2RGB)
        self.image = self.image_original_sample.copy()

        if self.center_sample and self.radius_sample > 0:
            cv2.circle(self.image, self.center_sample, self.radius_sample, (0, 150, 255), 2)

            mask = np.zeros_like(self.image_original_sample, dtype=np.uint8)
            cv2.circle(mask, self.center_sample, self.radius_sample, (255, 255, 255), -1)
            show = cv2.bitwise_and(self.image_original_sample, mask)

            self.display_image(show, self.parent.ui.show_pic_sample_sample)

        self.display_image(self.image, self.parent.ui.show_pic_real_sample)
        print("✅ Ảnh đã được cập nhật và hiển thị!")
       

    def read_value_file_back(self, file_name):
        points=[]
        with open(file_name, "r") as file:
            lines = file.readlines()

            if not lines:
                return []

            for line in lines:
                if line.strip():
                    x1, x2, x3 = map(int, line.strip().split())
                    points.append((x1, x2, x3))

                    self.center_sample= (x1,x2)
                    self.radius_sample= x3
                    self.update_display((0,150,255))
        return points
    
    def mouse_press_event(self, event):

        if not self.data_sample:
            """Xử lý sự kiện nhấn chuột."""

            if self.parent.ui.show_pic_real_sample.pixmap() is None :
                return
            
            x, y = self.convert_label_to_image_coords(event)

            # Kiểm tra nếu nhấn gần tâm hình tròn → Bật chế độ kéo
            if self.center_sample and self.radius_sample > 0:
                print(self.center_sample)
                distance = math.sqrt((x - self.center_sample[0]) ** 2 + (y - self.center_sample[1]) ** 2)
                if distance < self.radius_sample * 0.3:  # Nếu nhấn trong 30% bán kính hình tròn
                    self.dragging_sample = True
                    return

            # Nếu không nhấn vào hình tròn, vẽ hình mới
            self.center_sample = (x, y)
            self.radius_sample = 0
            self.dragging_sample = False
            self.image = self.image_original_sample.copy()
            self.display_image(self.image, self.parent.ui.show_pic_real_sample)

    def convert_label_to_image_coords(self, event):
        """Chuyển đổi tọa độ từ QLabel về tọa độ thực trong ảnh gốc."""
        label_width = self.parent.ui.show_pic_real_sample.width()
        label_height = self.parent.ui.show_pic_real_sample.height()
        img_height, img_width, _ = self.image_original_sample.shape

        scale_x = img_width / label_width
        scale_y = img_height / label_height

        x = int(event.pos().x() * scale_x)
        y = int(event.pos().y() * scale_y)
        return x, y
    
    def mouse_move_event(self, event):
        if not self.data_sample:
            self.temporary_sample=[]
            """Xử lý sự kiện kéo chuột."""
            if self.parent.ui.show_pic_real_sample.pixmap() is None:
                return

            x, y = self.convert_label_to_image_coords(event)

            if self.dragging_sample:
                # Di chuyển hình tròn thay vì vẽ lại
                self.center_sample = (x, y)
            elif self.center_sample:
                # Vẽ hình tròn mới nếu không kéo
                self.radius_sample = int(math.sqrt((x - self.center_sample[0]) ** 2 + (y - self.center_sample[1]) ** 2))

            self.temporary_sample.append((self.center_sample[0], self.center_sample[1], self.radius_sample))

            # Cập nhật ảnh
            self.update_display()

    def update_display(self, color=(255, 0, 0)):
        """Cập nhật QLabel với hình tròn hiện tại."""
        self.image = self.image_original_sample.copy()
        if self.center_sample and self.radius_sample > 0:
            cv2.circle(self.image, self.center_sample, self.radius_sample, color, 2)

            # Tạo mặt nạ và hiển thị vùng trong hình tròn trên QLabel `out`
            mask = np.zeros_like(self.image_original_sample, dtype=np.uint8)
            cv2.circle(mask, self.center_sample, self.radius_sample, (255, 255, 255), -1)
            show = cv2.bitwise_and(self.image_original_sample, mask)

            self.display_image(show, self.parent.ui.show_pic_sample_sample)
            # Hình ảnh vùng cần lấy
            # Mở rộng kích thước mặt nạ hình vuông
            expand_size = self.radius_sample + 2  # Tăng kích thước 10px so với hình tròn
            x1 = max(0, self.center_sample[0] - expand_size)
            y1 = max(0, self.center_sample[1] - expand_size)
            x2 = min(self.image_original_sample.shape[1], self.center_sample[0] + expand_size)
            y2 = min(self.image_original_sample.shape[0], self.center_sample[1] + expand_size)
            self.masked_image = show[y1:y2, x1:x2].copy()

            # cv2.imwrite('ok1.png',masked_image)
        self.display_image(self.image, self.parent.ui.show_pic_real_sample)

    def display_image(self, image, label):
        """Hiển thị ảnh OpenCV trên QLabel."""
        h, w, ch = image.shape
        bytes_per_line = ch * w
        q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(q_image))
        label.setScaledContents(True)  # Đảm bảo ảnh vừa với QLabel

    def mouse_release_event(self, event):
        """Xử lý sự kiện nhả chuột."""
        self.dragging_sample = False  # Dừng kéo hình tròn

    def function_button_take_sample(self):
        # if not self.temporary:
        self.data_sample= self.temporary_sample
        ## Saving data into local
        data_backup_write=open(self.point_circle_back_path,"w")
        data_all_write = ""
        for point in self.data_sample:
            data_all_write += f"{point[0]} {point[1]} {point[2]}"
        data_backup_write.write(data_all_write)
        data_backup_write.close()
        
        self.update_display((0,150,255))
        link = os.path.join(self.current_file_path, "picture", "saved_sample.png")
        cv2.imwrite(link,self.masked_image)
    
    def function_button_clear_sample(self):
        self.data_sample= []
        data_backup_write=open(self.point_circle_back_path,"w")
        data_all_write = ""
        for point in self.data_sample:
            data_all_write += f"{point[0]} {point[1]} {point[2]}"
        data_backup_write.write(data_all_write)
        data_backup_write.close()

        # self.center= (x1,x2)
        self.radius_sample= 0

        self.update_display()
        self.parent.ui.show_pic_sample_sample.clear()
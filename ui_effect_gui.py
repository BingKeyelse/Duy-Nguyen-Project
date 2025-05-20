from import_all import*

class UI_of_main_gui(MainWindow):
    # Thay đôi các màn hình đi kèm với mỗi nút 
    def change_window(self):
        # Mảng gồm các nút nhấn đi kèm
        buttons = [
            self.ui.but_tool_cam1, self.ui.but_tool_calib, self.ui.but_tool_4cam,
            self.ui.but_tool_sample, self.ui.but_tool_ng1cam, self.ui.but_tool_ng4cam,
            self.ui.but_tool_output, self.ui.but_tool_view
        ]
        for button in buttons:
            button.clicked.connect(lambda: UI_of_main_gui.toggle_visibility(self))

    def toggle_visibility(self):
        print('cos thay doi')
        self.ui.window_expand.setVisible(not self.ui.window_expand.isVisible())
        self.ui.window_icon.setVisible(not self.ui.window_icon.isVisible())

    # Chuyển đổi giữa các màn hình
    def tranfer_window(self):
         
         """Gán sự kiện cho các nút chuyển giữa các stackedWidget"""
         mapping = {
            self.ui.but_view_expand: self.ui.window_0,
            self.ui.but_view_icon: self.ui.window_0,
            self.ui.but_cam_1_expand: self.ui.window_1,
            self.ui.but_cam_1_icon: self.ui.window_1,
            self.ui.but_calib_cam1: self.ui.window_2,
            self.ui.but_take_sample_cam1: self.ui.window_3,
            self.ui.but_4_cam_expand: self.ui.window_4,
            self.ui.but_4_cam_icon: self.ui.window_4,
            self.ui.but_NG_1_expand: self.ui.window_5,
            self.ui.but_NG_1_icon: self.ui.window_5,
            self.ui.but_NG_4_expand: self.ui.window_6,
            self.ui.but_NG_4_icon: self.ui.window_6,
            self.ui.but_output_expand: self.ui.window_7,
            self.ui.but_output_icon: self.ui.window_7,
            self.ui.but_information_expand: self.ui.window_8,
            self.ui.but_information_icon: self.ui.window_8,
            self.ui.but_back_home_calib: self.ui.window_1,
            self.ui.but_back_home_sample: self.ui.window_1
            }

         for button, widget in mapping.items():
            button.clicked.connect(lambda _, w=widget: self.ui.stackedWidget.setCurrentWidget(w))
    
    # Chương trình chạy cập nhập thời gian và cập nhập ram và bộ nhớ
    def update_ram_and_disk_time_and_date(self):

        self.ram=0
        self.disk=0
        # Setup ban đầu với thời gian và thông số máy tính ngay ban đầu
        UI_of_main_gui.update_info_time_date(self)
        UI_of_main_gui.update_info_disk_ram(self)

        # cập nhập thời gian sau 1s
        self.timer0 = QTimer(self)
        self.timer0.timeout.connect(lambda: UI_of_main_gui.update_info_time_date(self))
        self.timer0.start(1000)  

        # cập nhập ram và disk sau 5s
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(lambda: UI_of_main_gui.update_info_disk_ram(self))
        self.timer1.start(5000)  

    
    # Cập nhập thông tin thời gian
    def update_info_time_date(self):

        """Hàm cập nhật thời gian vào QDateTimeEdit"""
        current_time = QDateTime.currentDateTime()
        self.ui.time_and_day.setDateTime(current_time)

    # Cập nhập disk và ram
    def update_info_disk_ram(self):
        """Hàm cập nhật thông tin RAM và Disk"""
        self.ram = psutil.virtual_memory()
        self.disk = psutil.disk_usage('/')

        ram_text =  f"RAM: {self.ram.percent}%"
        disk_text = f"Disk: {self.disk.percent}%"

        self.ui.show_ram_header.setText(f'{ram_text}')
        self.ui.show_disk_header.setText(f'{disk_text}')
    
    # Show ảnh màu lên label
    def show_image_3chanel(self,image,label):
        # """Hiển thị ảnh OpenCV trên QLabel."""
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Chuyển BGR -> RGB
        h, w, ch = image.shape
        bytes_per_line = ch * w
        q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)

        label.setPixmap(QPixmap.fromImage(q_image))  # Gán ảnh vào QLabel
        label.setScaledContents(True)  # Ảnh tự co giãn theo QLabel
        
    # Show ảnh nhị phân lên label
    def show_image_1chanel(self,image,label):
        """Hiển thị ảnh OpenCV trên QLabel."""
        initial_size = label.size()  # Kích thước QLabel
        # label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        resized_img = cv2.resize(image, (initial_size.width(), initial_size.height()), interpolation=cv2.INTER_LINEAR)

        img_height, img_width = resized_img.shape
        q_image = QImage(resized_img.data, img_width, img_height, img_width , QImage.Format.Format_Grayscale8)
        label.setPixmap(QPixmap.fromImage(q_image))

    # Lấy tên và link theo ngày giờ
    def give_name_file(self,path_link):
        name=str(datetime.now())[0:19].replace(":", "-").replace(" ", "_") + ".png"
        return name, os.path.join(path_link, name)
    
    def give_name_special(self):
        name=str(datetime.now())[0:19].replace(":", "-").replace(" ", "_") + ".png"
        return name
    
    def screen_real_4cam(self):
        self.ui.space_screen1_4cam.setCurrentWidget(self.ui.space_real_1_4cam)
        self.ui.space_screen2_4cam.setCurrentWidget(self.ui.space_real_2_4cam)
        self.ui.space_screen3_4cam.setCurrentWidget(self.ui.space_real_3_4cam)
        self.ui.space_screen4_4cam.setCurrentWidget(self.ui.space_real_4_4cam)
    
    def screen_result_4cam(self):
        self.ui.space_screen1_4cam.setCurrentWidget(self.ui.space_result_1_4cam)
        self.ui.space_screen2_4cam.setCurrentWidget(self.ui.space_result_2_4cam)
        self.ui.space_screen3_4cam.setCurrentWidget(self.ui.space_result_3_4cam)
        self.ui.space_screen4_4cam.setCurrentWidget(self.ui.space_result_4_4cam)





    

  
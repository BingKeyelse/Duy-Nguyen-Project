from import_all import*

class Cam_1(MainWindow):
    def __init__(self):
        super().__init__()
        
    # Bắt đầu đọc các file đã lưu và gán định giá trị ương tứng
    def start(self):
        path_folder=os.path.join(self.current_file_path,'data_txt','value_cam1.txt')
        
        self.value_saved_cam1=self.read_file(path_folder)
        self.value_saved_cam1= self.exchange_data(self.value_saved_cam1)

        self.value_now_cam1= self.value_saved_cam1.copy()

        Cam_1.update_slider_cam1(self,self.value_now_cam1)
        Cam_1.update_text_cam1(self,self.value_now_cam1)

        path_folder=os.path.join(self.current_file_path,'data_txt','value_cam2.txt')
        self.value_4cam=self.read_file(path_folder)
        self.value_4cam= self.exchange_data(self.value_4cam)

        Cam_1.update_slider_4cam(self,self.value_4cam)
        Cam_1.update_text_4cam(self,self.value_4cam)

    # Return lại giá trị mà lưu trước đó
    def undo_data(self):
        self.value_now_cam1=self.value_saved_cam1.copy()
        # print(f'Sư thay doi: {self.value_now_cam1}')

        Cam_1.update_slider_cam1(self,self.value_saved_cam1.copy())
        Cam_1.update_text_cam1(self,self.value_saved_cam1.copy())

    # Lưu giá trị lại để sài cho cho xử lý
    def save_data(self):
        self.value_saved_cam1=self.value_now_cam1.copy()

        Cam_1.update_slider_cam1(self,self.value_saved_cam1)
        Cam_1.update_text_cam1(self,self.value_saved_cam1)

        Cam_1.update_value_file_cam1(self)

    # Mỗi khi slider ở GUI cam 1 thay đổi sẽ định lại giá trị và cập nhập
    def slider_change_value_cam1(self):

        self.ui.slider_h_high_cam1.valueChanged.connect(lambda: Cam_1.define_value_cam1(self))
        self.ui.slider_s_high_cam1.valueChanged.connect(lambda: Cam_1.define_value_cam1(self))
        self.ui.slider_v_high_cam1.valueChanged.connect(lambda: Cam_1.define_value_cam1(self))

        self.ui.slider_h_low_cam1.valueChanged.connect(lambda: Cam_1.define_value_cam1(self))
        self.ui.slider_s_low_cam1.valueChanged.connect(lambda: Cam_1.define_value_cam1(self))
        self.ui.slider_v_low_cam1.valueChanged.connect(lambda: Cam_1.define_value_cam1(self))

        self.ui.slider_bright_cam1.valueChanged.connect(lambda: Cam_1.define_value_cam1(self))
        self.ui.show_value_contrast_cam1.editingFinished.connect(lambda: Cam_1.define_value_cam1(self))
        self.ui.slider_ratio_cam1.valueChanged.connect(lambda: Cam_1.define_value_cam1(self))
        self.ui.slider_r_circle_cam1.valueChanged.connect(lambda: Cam_1.define_value_cam1(self))
        self.ui.slider_limit_area_cam1.valueChanged.connect(lambda: Cam_1.define_value_cam1(self))

    # Gán giá trị cho cho cam 1
    def define_value_cam1(self):
        self.value_now_cam1[0]=int(self.ui.slider_h_high_cam1.value())
        self.value_now_cam1[1]=int(self.ui.slider_s_high_cam1.value())
        self.value_now_cam1[2]=int(self.ui.slider_v_high_cam1.value())
        
        self.value_now_cam1[3]=int(self.ui.slider_h_low_cam1.value())
        self.value_now_cam1[4]=int(self.ui.slider_s_low_cam1.value())
        self.value_now_cam1[5]=int(self.ui.slider_v_low_cam1.value())

        self.value_now_cam1[6]=int(self.ui.slider_bright_cam1.value())
        self.value_now_cam1[7]=Cam_1.check_value_line_edit(self)
        self.value_now_cam1[8]=int(self.ui.slider_ratio_cam1.value())
        self.value_now_cam1[9]=int(self.ui.slider_r_circle_cam1.value())
        self.value_now_cam1[10]=int(self.ui.slider_limit_area_cam1.value())

        Cam_1.update_slider_cam1(self,self.value_now_cam1)
        Cam_1.update_text_cam1(self,self.value_now_cam1)

        # self.process_cam_1(self.value_now_cam1)
        self.slider_timer1.start(100)# Bắt đầu timer chỉ cập nhập sau 0.1s

    # Gán giá trị cho 4 cam
    def define_value_4cam(self):
        self.value_4cam[0]=int(self.ui.slider_limit_area_4cam.value())

        Cam_1.update_slider_4cam(self,self.value_4cam)
        Cam_1.update_text_4cam(self,self.value_4cam)
        Cam_1.update_value_file_4cam(self)

        self.slider_timer2.start(10)# Bắt đầu timer chỉ cập nhập sau 0.01s

    # Check xem có phải số nguyên INT không với riêng phần Sản lượng
    def check_value_line_edit_production(self):
        value= self.ui.lineEdit.text()
        if Cam_1.Check_convert_str_to_int(self,value)==True:
            return int(value)
        else:
            return 0

    # Check xem có là giá trị float không nếu không cho về bằng 0.0 đặc biệt với QlineEdit
    def check_value_line_edit(self):
        value= self.ui.show_value_contrast_cam1.text()
        if Cam_1.Check_convert_str_to_float(self,value)==True:
            if float(value) >=0 and float(value) <=3:
                return float(value)
            else:
                return 0.0
        else:
            return 0.0
        
    # Chuyển xem có chuyển được string sang FLOAT không
    def Check_convert_str_to_float(self,number_check):
        try:
            float(number_check)
            return True
        except ValueError:
            return False
        
    # Chuyển xem có chuyển được string sang INT không
    def Check_convert_str_to_int(self,number_check):
        try:
            int(number_check)
            return True
        except ValueError:
            return False

    # Cập nhập giá trị slider ở trong GUI Cam 1
    def update_slider_cam1(self,value):
        self.ui.slider_h_high_cam1.setValue(value[0])
        self.ui.slider_s_high_cam1.setValue(value[1])
        self.ui.slider_v_high_cam1.setValue(value[2])

        self.ui.slider_h_low_cam1.setValue(value[3])
        self.ui.slider_s_low_cam1.setValue(value[4])
        self.ui.slider_v_low_cam1.setValue(value[5])

        self.ui.slider_bright_cam1.setValue(value[6])
        # self.ui.show_value_contrast_cam1.setText(str(value[7])) # Vì đây là QlineEdit
        self.ui.slider_ratio_cam1.setValue(value[8])
        self.ui.slider_r_circle_cam1.setValue(value[9])
        self.ui.slider_limit_area_cam1.setValue(value[10])

    # Cập nhập giá trị slider ở trong GUI 4 Cam
    def update_slider_4cam(self,value):
        self.ui.slider_limit_area_4cam.setValue(value[0])

    # Cập nhập giá trị label ở trong GUI Cam 1
    def update_text_cam1(self,value):
        self.ui.show_h_high_cam1.setText(f'H cao: {value[0]}')
        self.ui.show_s_high_cam1.setText(f'S cao: {value[1]}')
        self.ui.show_v_high_cam1.setText(f'V cao: {value[2]}')

        self.ui.show_h_low_cam1.setText(f'H thấp: {value[3]}')
        self.ui.show_s_low_cam1.setText(f'S thấp: {value[4]}')
        self.ui.show_v_low_cam1.setText(f'v thấp: {value[5]}')

        self.ui.show_bright_cam1.setText(f'Độ sáng: {value[6]}')
        if value[7]!= None:
            self.ui.show_value_contrast_cam1.setText(str(value[7]))
        else:
            self.ui.show_value_contrast_cam1.clear()
        self.ui.show_ratio_cam1.setText(f'Ngưỡng điểm NG: {value[8]}')
        self.ui.show_r_circle_cam1.setText(f'Delta R: {value[9]}')
        self.ui.show_limit_area_cam1.setText(f'Diện tích cho phép:: {value[10]}')

    # Cập nhập giá trị label ở trong GUI 4 Cam
    def update_text_4cam(self,value):
        self.ui.show_limit_area_4cam.setText(f'Ngưỡng phân định: {value[0]}')

    # Lưu giá trị cam 1 vào file 
    def update_value_file_cam1(self):
        path_folder=os.path.join(self.current_file_path,'data_txt','value_cam1.txt')
        data=open(path_folder, "w")
        data_all_cam1 = [ str(self.value_now_cam1[0])+"\n"+
                          str(self.value_now_cam1[1])+"\n"+
                          str(self.value_now_cam1[2])+"\n"+
                          str(self.value_now_cam1[3])+"\n"+
                          str(self.value_now_cam1[4])+"\n"+
                          str(self.value_now_cam1[5])+"\n"+
                          str(self.value_now_cam1[6])+"\n"+
                          str(self.value_now_cam1[7])+"\n"+
                          str(self.value_now_cam1[8])+"\n"+
                          str(self.value_now_cam1[9])+"\n"+
                          str(self.value_now_cam1[10])+"\n"
                    ]
        
        data.writelines(data_all_cam1)
        data.close()

    # Lưu giá trị 4 cam vào file 
    def update_value_file_4cam(self):
        path_folder=os.path.join(self.current_file_path,'data_txt','value_cam2.txt')
        data=open(path_folder, "w")
        data_all_4cam = [ str(self.value_4cam[0])+"\n"
                    ]
        
        data.writelines(data_all_4cam)
        data.close()
    
    # Chuyển đổi giữa các trang với cam 1
    def switch_page(self):

        """Chuyển đổi giữa hai trang"""
        current_index = self.ui.stackedWidget_2.currentIndex()
        # new_index = 1 if current_index == 0 else 0  # Nếu 0 → 1, nếu 1 → 0
        new_index = (current_index + 1) % 3  # Xoay vòng qua 0 → 1 → 2 → 0
        self.ui.stackedWidget_2.setCurrentIndex(new_index)
    
    def switch_page_right(self):
        """Chuyển đổi giữa hai trang"""
        # current_index = self.ui.stackedWidget_2.currentIndex()
        # new_index = 1 if current_index == 0 else 0  # Nếu 0 → 1, nếu 1 → 0
        # self.ui.stackedWidget_2.setCurrentIndex(new_index)

        current_index = self.ui.space_screen1_ng4cam.currentIndex()
        if current_index ==0:
            new_index = (current_index + 1)  # Xoay vòng qua 0 → 1 →

            self.ui.space_screen1_ng4cam.setCurrentIndex(new_index)
            self.ui.space_screen2_ng4cam.setCurrentIndex(new_index)
            self.ui.space_screen3_ng4cam.setCurrentIndex(new_index)
            self.ui.space_screen4_ng4cam.setCurrentIndex(new_index)
    
    def switch_page_left(self):
        """Chuyển đổi giữa hai trang"""
        # current_index = self.ui.stackedWidget_2.currentIndex()
        # new_index = 1 if current_index == 0 else 0  # Nếu 0 → 1, nếu 1 → 0
        # self.ui.stackedWidget_2.setCurrentIndex(new_index)

        current_index = self.ui.space_screen1_ng4cam.currentIndex()
        if current_index ==1:
            new_index = (current_index - 1)  # Xoay vòng qua 0 → 1 →

            self.ui.space_screen1_ng4cam.setCurrentIndex(new_index)
            self.ui.space_screen2_ng4cam.setCurrentIndex(new_index)
            self.ui.space_screen3_ng4cam.setCurrentIndex(new_index)
            self.ui.space_screen4_ng4cam.setCurrentIndex(new_index)

    

        

        


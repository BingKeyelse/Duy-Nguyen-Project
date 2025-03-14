from import_all import*

class Cam_1(MainWindow):
    def __init__(self):
        super().__init__()
        

    def start(self):
        path_folder=os.path.join(self.current_file_path,'data_txt','value_cam1.txt')
        
        self.value_saved_cam1=self.read_file(path_folder)
        self.value_saved_cam1= self.exchange_data(self.value_saved_cam1)

        self.value_now_cam1= self.value_saved_cam1.copy()
        Cam_1.update_slider_cam1(self,self.value_now_cam1)
        Cam_1.update_text_cam1(self,self.value_now_cam1)

    def undo_data(self):
        # print(self.value_now_cam1)
        # print(self.value_saved_cam1)
        self.value_now_cam1=self.value_saved_cam1.copy()
        print(f'Sư thay doi: {self.value_now_cam1}')

        Cam_1.update_slider_cam1(self,self.value_saved_cam1.copy())
        Cam_1.update_text_cam1(self,self.value_saved_cam1.copy())



    def save_data(self):
        self.value_saved_cam1=self.value_now_cam1.copy()

        Cam_1.update_slider_cam1(self,self.value_saved_cam1)
        Cam_1.update_text_cam1(self,self.value_saved_cam1)

        Cam_1.update_value_file_cam1(self)



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

        Cam_1.update_slider_cam1(self,self.value_now_cam1)
        Cam_1.update_text_cam1(self,self.value_now_cam1)

        # self.process_cam_1(self.value_now_cam1)
        self.slider_timer.start(100)



    def check_value_line_edit(self):
        value= self.ui.show_value_contrast_cam1.text()
        if Cam_1.Check_convert_str_to_float(self,value)==True:
            if float(value) >=0 and float(value) <=3:
                return float(value)
            else:
                return 0.0
        else:
            return 0.0

    def Check_convert_str_to_float(self,number_check):
        try:
            float(number_check)
            return True
        except ValueError:
            return False

    def update_slider_cam1(self,value):
        self.ui.slider_h_high_cam1.setValue(value[0])
        self.ui.slider_s_high_cam1.setValue(value[1])
        self.ui.slider_v_high_cam1.setValue(value[2])

        self.ui.slider_h_low_cam1.setValue(value[3])
        self.ui.slider_s_low_cam1.setValue(value[4])
        self.ui.slider_v_low_cam1.setValue(value[5])

        self.ui.slider_bright_cam1.setValue(value[6])
        # self.ui.show_value_contrast_cam1.setText(str(value[7]))
        self.ui.slider_ratio_cam1.setValue(value[8])
        self.ui.slider_r_circle_cam1.setValue(value[9])

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
                          str(self.value_now_cam1[9])+"\n"
                    ]
        
        data.writelines(data_all_cam1)
        data.close()
    
    def switch_page(self):
        """Chuyển đổi giữa hai trang"""
        # current_index = self.ui.stackedWidget_2.currentIndex()
        # new_index = 1 if current_index == 0 else 0  # Nếu 0 → 1, nếu 1 → 0
        # self.ui.stackedWidget_2.setCurrentIndex(new_index)

        current_index = self.ui.stackedWidget_2.currentIndex()
        new_index = (current_index + 1) % 3  # Xoay vòng qua 0 → 1 → 2 → 0
        self.ui.stackedWidget_2.setCurrentIndex(new_index)

        

        


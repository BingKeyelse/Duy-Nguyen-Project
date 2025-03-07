from import_all import*

class UI_of_main_gui(MainWindow):
    def change_window(self):
        self.ui.but_tool_cam1.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_calib.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_4cam.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_take.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_ng1cam.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_ng4cam.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_output.clicked.connect(self.toggle_visibility)

    def tranfer_window(self):
        self.ui.but_cam_1_expand.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_1))
        self.ui.but_cam_1_icon.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_1))

        self.ui.but_calib_cam1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_2))

        self.ui.but_take_sample_cam1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_3))

        self.ui.but_4_cam_expand.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_4))
        self.ui.but_4_cam_icon.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_4))

        self.ui.but_NG_1_expand.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_5))
        self.ui.but_NG_1_icon.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_5))

        self.ui.but_NG_4_expand.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_6))
        self.ui.but_NG_4_icon.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_6))

        self.ui.but_output_expand.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_7))
        self.ui.but_output_icon.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.window_7))
        
    

  
from import_all import*

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        
        self.ui.window_expand.hide()

        #### Funtion UI
        UI_of_main_gui.update_ram_and_disk_time_and_date(self)
        UI_of_main_gui.change_window(self)
        UI_of_main_gui.tranfer_window(self)

        


        #
        self.ram=0
        self.disk=0

        


    # def update_time_and_date(self):
        

    def toggle_visibility(self):
        self.ui.window_expand.setVisible(not self.ui.window_expand.isVisible())
        self.ui.window_icon.setVisible(not self.ui.window_icon.isVisible())

if __name__ == "__main__":
    ### Convert 
    auto_tranfer_file.convert_ui_qrc_to_py()
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

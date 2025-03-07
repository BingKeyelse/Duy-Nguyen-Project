from import_all import*
from main_gui import Ui_MainWindow  # Import file giao diện PyQt5

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.read_and_update_time_date()
        UI_of_main_gui.change_window(self)
        
        self.ui.window_expand.hide()


        # Tạo QTimer để cập nhật thời gian mỗi giây
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1000ms = 1 giây

        #
        self.ram=0
        self.disk=0

        

    def read_and_update_time_date(self):
        # Initial setup time and date with GUI
        self.update_info()
        # Tạo QTimer để cập nhật mỗi phút (60000 ms)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        self.timer.start(30000)  # Update after 30s


    def update_info(self):
        """Hàm cập nhật thông tin RAM và Disk"""
        self.ram = psutil.virtual_memory()
        self.disk = psutil.disk_usage('/')

        ram_text = f"RAM: {self.ram.percent}% ({self.ram.used / 1e9:.2f} GB / {self.ram.total / 1e9:.2f} GB)"
        disk_text = f"Disk: {self.disk.percent}% ({self.disk.used / 1e9:.2f} GB / {self.disk.total / 1e9:.2f} GB)"

        self.ui.show_ram_header.setText(f'Ram: {ram_text}')
        self.ui.show_disk_header.setText(f'Disk: {disk_text}')

    def update_time(self):
        """Hàm cập nhật thời gian vào QDateTimeEdit"""
        current_time = QDateTime.currentDateTime()
        self.ui.time_and_day.setDateTime(current_time)

    def toggle_visibility(self):
        self.ui.window_expand.setVisible(not self.ui.window_expand.isVisible())
        self.ui.window_icon.setVisible(not self.ui.window_icon.isVisible())

if __name__ == "__main__":
    ### Convert 
    convert_ui_qrc_to_py()
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

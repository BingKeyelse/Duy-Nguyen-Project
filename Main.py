import sys
import os
# os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"  # Tắt auto-scaling DPI
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"
import cv2
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtGui import QImage, QPixmap
from multiprocessing import Queue
import queue
from pypylon import pylon
import threading
import psutil


from main_gui import Ui_MainWindow  # Import file giao diện PyQt5

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.update_info()
        self.ui.window_expand.hide()

        self.ui.but_tool_cam1.clicked.connect(self.toggle_visibility)

        # Tạo QTimer để cập nhật thời gian mỗi giây
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1000ms = 1 giây

        #
        self.ram=0
        self.disk=0

        # Tạo QTimer để cập nhật mỗi phút (60000 ms)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        self.timer.start(60000)  # Cập nhật sau mỗi 60 giây

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
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

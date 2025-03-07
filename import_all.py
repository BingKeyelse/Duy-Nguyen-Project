# ===== Thư viện chuẩn của Python =====
import os
import sys
import time
import threading
import queue
from multiprocessing import Queue
import psutil
import subprocess


# ===== Thiết lập môi trường cho Qt trước khi import PyQt5 =====
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"

# ===== Thư viện bên thứ ba =====
import cv2
from pypylon import pylon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtGui import QImage, QPixmap

# ===== Module nội bộ của dự án =====
import  auto_tranfer_file 
from Main import MainWindow
from ui_effect_gui import UI_of_main_gui
from main_gui import Ui_MainWindow

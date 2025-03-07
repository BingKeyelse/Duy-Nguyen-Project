import sys
import os
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"  # Tắt auto-scaling DPI
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
from auto_tranfer_file import*
from Main import*
from ui_effect_gui import*
from auto_tranfer_file import*
from main_gui import Ui_MainWindow  # Import file giao diện PyQt5


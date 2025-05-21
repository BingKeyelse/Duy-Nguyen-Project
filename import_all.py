# ===== Thư viện chuẩn của Python =====
import os
import sys
import sys
# sys.exit()                                                                                                                                                                                                    
import time
import threading
import queue
from multiprocessing import Queue, Value
import psutil
import subprocess
from natsort import natsorted
import codecs, json
import numpy as np
import matplotlib.image as mpimg
import glob
import math
from datetime import datetime
import shutil
import sqlite3
from multiprocessing import Process, Value, Queue , Manager
import multiprocessing
import gc
import random

os.environ["GENICAM_GENTL64_PATH"] = os.path.abspath("opt/pylon/lib/gentlproducer/gtl")
os.environ["PYLON_GENICAM_PRODUCER"] = "Gt"
os.environ["PYLON_ROOT"] = os.path.abspath("opt/pylon")

print("GENICAM_GENTL64_PATH =", os.environ.get("GENICAM_GENTL64_PATH"))



# ===== Thiết lập môi trường cho Qt trước khi import PyQt5 =====
# os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
# os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
# os.environ["QT_SCALE_FACTOR"] = "1"
# os.environ["QT_IM_MODULE"] = "compose"

# ===== Thư viện bên thứ ba =====
import cv2
from pypylon import pylon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy, QLayout, QTableWidgetItem, QWidget, QHBoxLayout, QDialog
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
import icons_rc

# ====== Thu vien chay AI ============
## Run with ONNX file
try:
    import onnxruntime as ort
except ModuleNotFoundError:
    raise ImportError("The 'onnxruntime' module is not installed. Please install it with 'pip install onnxruntime' before running this script.")

# ===== Module nội bộ của dự án =====
import  auto_tranfer_file 
from main_gui import Ui_MainWindow
from popup import Ui_Dialog
from Main import MainWindow
from ui_effect_gui import UI_of_main_gui
from calib_function import Calib
from cam1_function import Cam_1
from sample_function import Sample
from listWidget_function import ListWidget

# =================================



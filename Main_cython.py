#!/usr/bin/env python3
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
from collections import deque

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
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy, QLayout, \
    QTableWidgetItem, QWidget, QHBoxLayout, QDialog
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
import icons_rc

# ====== Thu vien chay AI ============
## Run with ONNX file
try:
    import onnxruntime as ort
except ModuleNotFoundError:
    raise ImportError("The 'onnxruntime' module is not installed. Please install it with 'pip install onnxruntime' before running this script.")

from main_gui import Ui_MainWindow
from popup import Ui_Dialog

class SubWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Dialog()
        self.setupUi(self)  

        # Hide layout
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Unable some function of others 
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.setupUi(self)
        self.ui.but_no.clicked.connect(self.close)  # Gán sự kiện đóng cửa sổ
        self.ui.but_yes.clicked.connect(self.close)  # Gán sự kiện đóng cửa sổ phụ
        self.ui.but_yes.clicked.connect(self.parent.close)  # Gán sự kiện đóng cửa sổ phụ

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showFullScreen()  # Hiển thị toàn màn hình
        # self.showMaximized()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Lấy đường dẫn tuyệt đối của file đang chạy 
        if getattr(sys, 'frozen', False):
            self.current_file_path = sys._MEIPASS
        else:
            self.current_file_path = os.path.dirname(os.path.abspath(__file__))

        # Tạo ra đường dẫn và thư mục hiện thời để lưu cho NG
        self.auto_check_and_create_folder_and_file_NG()

        # Kiểm tra xem có tháng trước đó không
        self.check_month_forth()
        
        # Khai báo các dữ liệu của cho sản phẩm OK, NG, tổng sản lượng, ...
        self.value_const_production= 0
        self.value_const_production_new= 0
        self.value_ok_production= 0
        self.value_ng_production= 0
        self.end_date_production=''
        self.init_production()
        self.ui.lineEdit.editingFinished.connect(self.update_production)
        self.ui.but_save_output.clicked.connect(self.save_value_production)
        self.ui.but_again_output.clicked.connect(self.insert_new_data_into_database_production)

        # Tạo database với SQLite: data cam1, data 4cam, data theo dõi sản lượng
        self.database=['data_cam1.db','data_4cam.db']
        self.database_production=['data_production.db']
        self.create_or_check_database()

        # Update sau 50ms với màn hình thể hiện số lượng sản phẩm đang theo dõi
        self.timer_product=QTimer(self)
        self.timer_product.timeout.connect(self.monitor_production)
        self.timer_product.start(50)

        # Cập nhập time và date sau 60s để xem có thay đôi tháng không 
        self.timer_date = QTimer(self)
        self.timer_date.timeout.connect(self.monitor_month_change)
        self.timer_date.start(60000) 

        # Khởi động setup liên quan đết giao diện ban đầu để cố định một loạt các frame ảnh để nó sẽ không bị thay đổi 
        # kích thước ảnh mỗi khi có một tác động nhất định của các function
        self.initial_UI_setup()

        # Lấy giá trị các ma trận đã có được từ Calib cho việc sử dụng cho Calib ảnh sau khi lấy được từ  camera 
        json_path = os.path.join(self.current_file_path, "data_calib", "calib_camera.json")
        self.frame_calibrate = FrameCalibrate(json_path)
        
        # Liên kết Widget khi thay đổi thì sẽ cập nhập các giá trị để biết ảnh lấy sẽ đi đâu
        # vì từ cam 1 ta sẽ có 3 mục đích dùng:  Xử lý, Calib, Lấy mẫu
        self.ui.stackedWidget.currentChanged.connect(self.on_page_changed)

        # Chương trình nút nhấn thoát hệ thống
        # self.ui.but_exit_expand.clicked.connect(lambda: self.close())
        # self.ui.but_exit_icon.clicked.connect(lambda: self.close())
        self.ui.but_exit_expand.clicked.connect(self.popup_open)
        self.ui.but_exit_icon.clicked.connect(self.popup_open)

        ##### Cam 1
        # Khởi tạo data lưu trữ: queue với camera 1
        self.current_queue_cam1 = queue.Queue(maxsize=1)
        self.mode_pic_cam1= Value("i",0)  # 0: Cam 1, 1: Calib, 2: Sample
        self.image_sample_cam1=cv2.imread(os.path.join(self.current_file_path, "picture", "saved_sample.png"))

        ### Khai báo biến
        # H high, S high, V high, H low, S low, V low, bright, contrast, ratio, R circle, Limit area 
        self.value_saved_cam1=[None, None, None, None, None, None, None, None, None, None,None] 
        self.value_now_cam1=[None, None, None, None, None, None, None, None, None, None, None] 
        self.image_cam1=None
        self.image_process=None

        # Data 4 cam chạy AI
        self.value_4cam=[None] 

        # Khởi động cac thông số và dữ liệu liên quan đến cam 1, cập nhập đọc giá trị đã được lưu và gán giá trị cho các Silder và Label
        Cam_1.start(self)
        # Gọi chương trình để gán cho việc thay đổi giá trị với các Slider thì sẽ được liên kết với một chương trình xử lý trung tâm chúng
        # Cam 1
        Cam_1.slider_change_value_cam1(self)
        # 4 Cam
        self.ui.slider_limit_area_4cam.valueChanged.connect(lambda: Cam_1.define_value_4cam(self))


        ## Tạo một Timer liên kết với việc xử lý chương trình của cam 1 mỗi khi có thay đổi các slider và label giá trị
        #  chúng xử lý sau một khoảng thời gian kích hoạt để không làm cho việc thay đổi giá trị slider ảnh hưởng đến hiện suất
        #   khiến cho giao diện bị lag quá nhiều và lệnh kích hoạt chúng có liên quan đến hàm 
        #   Cam_1.define_value_cam1 và chúng kích hoạt chạy sau 0.1s lận
        #  và viết sao mỗi lần thay đổi giá trị cúng không xuất giá trị OK và NG vì bên PLC đang sài dịch mảng tối quan trọng trong 
        #  xử lý phần này, chỉ cho gửi giá trị khi mà chạy vào luồng lấy tự động bằng trigger( cả phần mềm và phần cứng)
        
        self.slider_timer1 = QTimer()
        self.slider_timer1.setSingleShot(True)
        self.slider_timer1.timeout.connect(lambda: self.process_cam_1(self.value_now_cam1))

        # Khai báo giá trị để chứa các ảnh của phần 4 cam AI gồm ảnh thực và ảnh binary
        #  lưu trữ và tác biệt chúng phục vụ cho mục đích gán sau khi lấy từ các queue ra
        self.image_cam2_4cam=None
        self.image_cam3_4cam=None
        self.image_cam4_4cam=None
        self.image_cam5_4cam=None

        self.image_binary_cam2_4cam= None
        self.image_binary_cam3_4cam= None
        self.image_binary_cam4_4cam= None
        self.image_binary_cam5_4cam= None

        ## Ý tưởng phần này làm cũng giống như phần trên chỉ gọi và gán chứ không kích hoạt chỉ chạy khi có thay đổi liên quan 
        #  đến các thanh Slider và Label giá trị ở phần giao diện của 4 cam tránh ảnh hưởng đến hiệu suất và tùy biến giá trị xuất ra
        #  vì phần nhận tín hiệu của 4 cam trên PLC cũng lưu trữ và để dịch bit
        self.slider_timer2 = QTimer()
        self.slider_timer2.setSingleShot(True)
        self.slider_timer2.timeout.connect(lambda: self.update_process_4cam_with_slider())

        # Gán chức năng nút nhấn cho mỗi nút nhấn nằm ở phần giao diện dành riêng cho Cam 1 
        self.ui.but_saving_cam1.clicked.connect(lambda: Cam_1.save_data(self))
        self.ui.but_undo_cam1.clicked.connect(lambda: Cam_1.undo_data(self))
        self.ui.but_take_picture_cam1.clicked.connect(self.trigger_cam_1)
        self.ui.but_right_ng4cam.clicked.connect(lambda: Cam_1.switch_page_right(self))
        self.ui.but_left_ng4cam.clicked.connect(lambda: Cam_1.switch_page_left(self))

        # Khai báo tâm của đối tượng matching với Cam 1 để sài cho mục đích vẽ 
        self.center_cam1=0

        # -----------------------------
        # -----------------------------

        ## Khởi tạo queue cho cam 2 3 4 5
        # AI
        self.queue_AI_cam2= Queue(maxsize=2)
        self.queue_AI_cam3= Queue(maxsize=2)
        self.queue_AI_cam4= Queue(maxsize=2)
        self.queue_AI_cam5= Queue(maxsize=2)
        # GUI
        self.queue_GUI_cam2= Queue(maxsize=1)
        self.queue_GUI_cam3= Queue(maxsize=1)
        self.queue_GUI_cam4= Queue(maxsize=1)
        self.queue_GUI_cam5= Queue(maxsize=1)
        

        # Khai báo bit cờ cho mục đích chạy AI, có thể thay bit này bằng Value trong mutilprocessing
        #   khi chương trình kết thúc thì ta đưa nó về False để không làm phá hủy chu trình đang chạy 
        #   của process đang chạy AI cho 4 cam
        self.maner= Manager()
        self.mode_run_AI=self.maner.Namespace()
        self.mode_run_AI.flag=True

        # Bit tín hiệu để xuất giá trị cho phần output bên camera lần lượt là cho Cam 1 và hệ 4 Cam
        self.mode_output_1   = Value("i",0)
        self.mode_output_2   = Value("i",0)

        # Value cho mode output cho từng cam 
        # Cam 1: chỉ cần một bit quy định để rồi từ đó thay đổi giá trị cho self.mode_output_1, nó sẽ 
        #   tự biết để điều chỉnh hàm output dành riêng cho Cam 1

        # 4 Cam: cần mảng để thể hiện 2 giá trị [hoàn thành xử lý, kết quả xử lý], ròi sau đó tổng
        #   hợp lại và truyền cho self.mode_output_2
        self.mode_cam1   = 0
        self.mode_cam2   = [0,0]
        self.mode_cam3   = [0,0]
        self.mode_cam4   = [0,0]
        self.mode_cam5   = [0,0]
        
        # Giá trị chứa các mảng chưa tập hợp ảnh và kết quả ảnh bị phân của AI sau xử lý gồm 4 ảnh mỗi mảng
        self.real_image_4cam=[]
        self.vitrual_image_4cam=[]

        # Mảng output tạo ra để lưu trữ kết quả từ cam 1 cho mục đích phù hợp với dịch bit bên PLC
        self.result_output_cam1=deque()
        self.result_output_4cam=0 # Tổng hợp kết quả của các giá trị 4 Cam sau khi nhận được toàn bộ

        # Giá trị để debug
        self.count_cam1=0
        self.count_4cam=0



        # ✅ Khởi tạo camera Basler
        self.camera = camera_Basler_multi(self.current_queue_cam1, self.queue_GUI_cam2, self.queue_GUI_cam3, self.queue_GUI_cam4, self.queue_GUI_cam5
                                          , self.mode_output_1, self.mode_output_2) # Chỉ có khi chuyển sang Calib là gửi số 0 đi do là 
                                                                                    # không thể lấy ảnh từ cơ cấu chuyển động mà phải lấy 
                                                                                    #  ảnh ma trận mà chính tay mình điều chỉnh cho phù hợp
        self.camera.begin()

        # ✅ Khởi tạo process đanh riêng cho AI
        self.process_AI = Process(target = run_AI, args=(self.mode_run_AI, self.queue_GUI_cam2, self.queue_GUI_cam3, self.queue_GUI_cam4, self.queue_GUI_cam5,
                                                    self.queue_AI_cam2, self.queue_AI_cam3, self.queue_AI_cam4, self.queue_AI_cam5,))
        self.process_AI.start()

        # Nút nhấn cho phần giao diện 4 Cam
        self.ui.but_real_4cam.clicked.connect(lambda: UI_of_main_gui.screen_real_4cam(self))
        self.ui.but_result_4cam.clicked.connect(lambda: UI_of_main_gui.screen_result_4cam(self))

        ##--------------------------------------------------
        ##--------------------------------------------------

        ## Calib
        # Chức năng của Calib
        Calib.start(self) # Khởi động ban đầu mà không chạy qua lệnh __init__
        self.ui.but_clear_calib.clicked.connect(lambda: Calib.clear_file_image(self))
        self.ui.but_take_calib.clicked.connect(self.trigger_cam_calib)
        self.ui.but_calib_calib.clicked.connect(self.auto_calib)
        

        ## Sample: dùng để lấy mẫu cho việc temple matching
        self.sample=Sample(self)
        self.ui.but_take_sample.clicked.connect(self.trigger_cam_sample)

        ##--------------------------------------------------
        ##--------------------------------------------------

        ## Load Listwidget
        # Cam1
        self.real_path_ng_cam1 = os.path.join(self.path_folder_today_ng_now_cam1, "real")
        self.virtual_path_ng_cam1 = os.path.join(self.path_folder_today_ng_now_cam1, "virtual")
        self.list_widget=ListWidget(self)
        self.ui.but_NG_1_expand.clicked.connect(self.list_widget.list_NG_cam1)
        self.ui.but_NG_1_icon.clicked.connect(self.list_widget.list_NG_cam1)
        self.ui.but_result_cam1.clicked.connect(lambda: Cam_1.switch_page(self))

        # 4cam
        self.real_path_ng_4cam = os.path.join(self.path_folder_today_ng_now_4cam, "real")
        self.virtual_path_ng_4cam = os.path.join(self.path_folder_today_ng_now_4cam, "virtual")
        self.ui.but_NG_4_expand.clicked.connect(self.list_widget.list_NG_4cam)
        self.ui.but_NG_4_icon.clicked.connect(self.list_widget.list_NG_4cam)

        ##--------------------------------------------------
        ##--------------------------------------------------

        # Hàm setup chức năng cho UI như nút nhấn, chuyển giao diện
        UI_of_main_gui.update_ram_and_disk_time_and_date(self)
        UI_of_main_gui.change_window(self)
        UI_of_main_gui.tranfer_window(self)

        # Tạo chức năng cho nút nhấn View
        self.ui.but_clear_data_production_restored.clicked.connect(self.clear_data_production_restored)
        self.ui.but_clear_data_production_restored_icon.clicked.connect(self.clear_data_production_restored)
        self.ui.but_clear_data_production_restored_expand.clicked.connect(self.clear_data_production_restored)
        self.ui.but_clear_data_ng_view.clicked.connect(self.clear_data_ng_restored)


        ##--------------------------------------------------
        ##--------------------------------------------------

        # Khai báo biến để chạy cho các vòng lặp để khi kil không làm sụp đổ hệ thống do bị tắt đột ngột
        self.running=True

        ## Các hàm threading
        # Cam 1
        self.thread1= threading.Thread(target=self.process_queue_cam1, daemon=True)
        self.thread1.start()

        # 4 cam
        # Gắn chức năng cho phép chụp trigger với nút trên giao diện cho 4 cam
        self.ui.but_real_4cam_2.clicked.connect(self.trigger_4cam)

        # Lần lượt là 4 thread gắn với mỗi 4 process khi nhận được ảnh từ xử lý AI
        #   để cho chúng tự nhận tự xử lý mà không phải giới hạn cho việc ảnh nào phải xử lý trước xử lý sau
        self.thread2= threading.Thread(target=self.process_queue_4cam_cam2, daemon=True)
        self.thread2.start()

        self.thread3= threading.Thread(target=self.process_queue_4cam_cam3, daemon=True)
        self.thread3.start()
        
        self.thread4= threading.Thread(target=self.process_queue_4cam_cam4, daemon=True)
        self.thread4.start()

        self.thread5= threading.Thread(target=self.process_queue_4cam_cam5, daemon=True)
        self.thread5.start()

        ## Nút nhấn Screenshot
        self.ui.but_screenshot_expand.clicked.connect(self.screen_shot)
        self.ui.but_screenshot_icon.clicked.connect(self.screen_shot)

    ##------------------------------------------------------------
    ##------------------------------------------------------------

    def check(self, *args, **kwargs):
        print(f'OKOKOKOKOK: {self.value_now_cam1}')
    
    def screen_shot(self, *args, **kwargs):
        """Chức năng chụp màn hình"""
        # Lấy màn hình chính
        screen = QApplication.primaryScreen()

        # Chụp và lưu
        screenshot = screen.grabWindow(0)  # 0 = toàn màn hình
        # Chuyển từ QPixmap sang QImage
        qimage = screenshot.toImage()
        # Lấy thông tin ảnh
        width = qimage.width()
        height = qimage.height()
        ptr = qimage.bits()
        ptr.setsize(qimage.byteCount())
        img = np.array(ptr).reshape(height, width, 4)  # RGBA

        # Chuyển sang BGR để dùng với OpenCV
        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        # screenshot=cv2.cvtColor(screenshot,cv2.COLOR_BGR2RGB)
        
        #Lấy tên cho ảnh
        source='/home/pronics/Desktop/Screenshot'
        _, link_path= UI_of_main_gui.give_name_file(self,source)

        # Lưu ảnh
        cv2.imwrite(link_path, img_bgr)

    def clear_data_ng_restored(self, *args, **kwargs):
        # Lấy thư mục hiện tại
        folder_path = os.path.join(self.current_file_path, "data_NG")

        # Lọc qua rồi xóa
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.remove(file_path)  # Xóa file hoặc symbolic link
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Xóa thư mục con
                except Exception as e:
                    print(f"Không thể xóa {file_path}: {e}")
                    sys.exit()
        
        # Xóa rồi thì tạo lại thư mục thôi
        self.auto_check_and_create_folder_and_file_NG()

        ## Làm mới lại cả database chứa đường dẫn
        # Xóa 2 database hiện chứa dữ liệu cũ
        link_databases=['data_cam1.db','data_4cam.db']
        for link_database in link_databases:
                db_path = os.path.join(self.current_file_path, "data_txt", link_database)
                if os.path.exists(db_path):
                    os.remove(db_path)
        
        # Tạo mới
        self.create_or_check_database()



    def clear_data_production_restored(self, *args, **kwargs):
        self.result_output_cam1.clear()

    def read_file(self, link): # dùng để đọc file text riêng cho phần đọc tháng
        data_read= open(link,"r")
        data=data_read.readlines()
        data_read.close()
        return data
    
    def exchange_data(self,data): # dùng để trao chuyển đổi data đạng biệt với phần tử thứ 7 
                                  #   phải đưa về float vì đó là một giá trị đặc biệt từ editLine
        processed = []
        for i, value in enumerate(data):
            try:
                if i == 7 :  # Phần tử thứ 7 -> float
                    processed.append(float(value))
                else:  # Các phần tử khác -> int
                    processed.append(int(value))
            except ValueError:
                processed.append(value)  # Nếu không chuyển được, giữ nguyên
        return processed

    def on_page_changed(self, *args, **kwargs): # gắn giá trị để không phải lúc nào cũng lấy ảnh từ trigger phần cứng 
                               #   để mỗi Widget cho Cam 1 sẽ làm một giá trị đặc biệt riêng
        """Cập nhật ảnh khi trang có QLabel xuất hiện"""
        if self.ui.stackedWidget.currentWidget() == self.ui.window_1:
            self.mode_pic_cam1.value=0
        elif self.ui.stackedWidget.currentWidget() == self.ui.window_2:
            # Sẽ chạy hàm liên kết sau 50ms chứ không chạy ngay lập tức
            QTimer.singleShot(50, lambda: Calib.check_file_in_folder(self))
            self.mode_pic_cam1.value=1
        elif self.ui.stackedWidget.currentWidget() == self.ui.window_3:
            self.mode_pic_cam1.value=2
        else:
            self.mode_pic_cam1.value=0
        
    def initial_UI_setup(self, *args, **kwargs):
        # Luôn ở màn hình View
        self.ui.stackedWidget.setCurrentIndex(0)

        # Đóng màn hình full icon
        self.ui.window_expand.hide()

        # Setup màn hình view
        self.ui.show_pic_cam_cam1_view.setFixedSize(425, 440)
        self.ui.show_pic_cam_4cam_view.setFixedSize(425, 440)

        # Setup màn Cam 1
        self.ui.show_pic_cam_cam1.setFixedSize(280, 280)
        self.ui.show_pic_thread_cam1.setFixedSize(280, 280)
        self.ui.show_pic_real_cam1.setFixedSize(280, 280)
        self.ui.show_pic_virtual_cam1.setFixedSize(280, 280)

        # Setup màn hinh listwidget cam 1 ng
        self.ui.show_pic_real_ng1cam.setFixedSize(300, 300)
        self.ui.show_pic_result_ng1cam.setFixedSize(300, 300)

        # Tạo QLabel mới trên nền của màn hình hiện ảnh của calib
        self.current_label = QLabel("          ", self.ui.show_pic_calib_calib)
        self.current_label.setStyleSheet("color: black; font-size: 16px;")
        self.ui.show_pic_calib_calib.setFixedSize(495, 492)

        # Setup màn Sample
        self.ui.show_pic_real_sample.setFixedSize(426, 508)
        self.ui.show_pic_sample_sample.setFixedSize(426, 508)

        # Setup man 4cam 
        self.ui.space_screen1_4cam.setCurrentWidget(self.ui.space_real_1_4cam)
        self.ui.space_screen2_4cam.setCurrentWidget(self.ui.space_real_2_4cam)
        self.ui.space_screen3_4cam.setCurrentWidget(self.ui.space_real_3_4cam)
        self.ui.space_screen4_4cam.setCurrentWidget(self.ui.space_real_4_4cam)

        self.ui.show_pic_real_1_4cam.setFixedSize(220,220)
        self.ui.show_pic_real_2_4cam.setFixedSize(220,220)
        self.ui.show_pic_real_3_4cam.setFixedSize(220,220)
        self.ui.show_pic_real_4_4cam.setFixedSize(220,220)

        self.ui.show_pic_result_1_4cam.setFixedSize(220,220)
        self.ui.show_pic_result_2_4cam.setFixedSize(220,220)
        self.ui.show_pic_result_3_4cam.setFixedSize(220,220)
        self.ui.show_pic_result_4_4cam.setFixedSize(220,220)

        # Setup man 4cam NG
        self.ui.space_screen1_ng4cam.setCurrentWidget(self.ui.space_real_1_ng4cam)
        self.ui.space_screen2_ng4cam.setCurrentWidget(self.ui.space_real_2_ng4cam)
        self.ui.space_screen3_ng4cam.setCurrentWidget(self.ui.space_real_3_ng4cam)
        self.ui.space_screen4_ng4cam.setCurrentWidget(self.ui.space_real_4_ng4cam)

        self.ui.show_pic_real_1_ng4cam.setFixedSize(220,220)
        self.ui.show_pic_real_2_ng4cam.setFixedSize(220,220)
        self.ui.show_pic_real_3_ng4cam.setFixedSize(220,220)
        self.ui.show_pic_real_4_ng4cam.setFixedSize(220,220)

        self.ui.show_pic_result_1_ng4cam.setFixedSize(220,220)
        self.ui.show_pic_result_2_ng4cam.setFixedSize(220,220)
        self.ui.show_pic_result_3_ng4cam.setFixedSize(220,220)
        self.ui.show_pic_result_4_ng4cam.setFixedSize(220,220)
        
    def trigger_cam_1(self, *args, **kwargs): # Lẩy ảnh với Cam 1 để xử lý
        self.mode_pic_cam1.value=0
        """Gọi trigger để chụp ảnh"""
        self.camera.trigger_cam_special()  

    def trigger_cam_sample(self, *args, **kwargs): # Lấy ảnh với Cam 1 để truyền vào chương trình Sample để Temple matching
        self.mode_pic_cam1.value=2
        """Gọi trigger để chụp ảnh"""
        self.camera.trigger_cam_special()

    def trigger_cam_calib(self, *args, **kwargs): # Lấy ảnh với Cam 1 để truyền vào chương trình Calib
        if self.file_count_calib <7: # Khi khởi tạo Calib thì biết này vì nó cập nhập theo Timer, lấy liên tục
            self.mode_pic_cam1.value=1 
            """Gọi trigger để chụp ảnh"""
            self.camera.trigger_cam_special()
        
    def trigger_4cam(self, *args, **kwargs): # Chụp ảnh với 4 Cam của AI
        self.camera.trigger_4cam()

    def update_process_4cam_with_slider(self, *args, **kwargs): # Hàm thay đổi giá trị 4 Cam AI khi thay đổi QSlider
        if (self.image_cam2_4cam is not None and
            self.image_cam3_4cam is not None and
            self.image_cam4_4cam is not None and
            self.image_cam5_4cam is not None):
            # print(self.value_4cam[0])
            value_2=[]
            value_3=[]
            value_4=[]
            value_5=[]
            _, value_2= self.process_queue_4cam_each_camera(self.image_cam2_4cam.copy(), self.image_binary_cam2_4cam.copy(),
                                                                self.ui.show_pic_real_1_4cam,self.ui.show_pic_result_1_4cam)
            
            _, value_3= self.process_queue_4cam_each_camera(self.image_cam3_4cam.copy(), self.image_binary_cam3_4cam.copy(),
                                                                self.ui.show_pic_real_2_4cam,self.ui.show_pic_result_2_4cam)
            
            _, value_4= self.process_queue_4cam_each_camera(self.image_cam4_4cam.copy(), self.image_binary_cam4_4cam.copy(),
                                                                self.ui.show_pic_real_3_4cam,self.ui.show_pic_result_3_4cam)
            
            _, value_5= self.process_queue_4cam_each_camera(self.image_cam5_4cam.copy(), self.image_binary_cam5_4cam.copy(),
                                                                self.ui.show_pic_real_4_4cam,self.ui.show_pic_result_4_4cam)

            if value_2[0]==2 or value_3[0]==2 or value_4[0]==2 or value_5[0]==2: # Xuat tin hieu NG và thay đổi label tương ứng
             
                self.ui.label_ok_4cam.setStyleSheet(f"background: #c6c6c6;")
                self.ui.label_ng_4cam.setStyleSheet(f"background: #ff0772;")
                        
            elif value_2[0]==1 and value_3[0]==1 and value_4[0]==1 and value_5[0]==1: # Xuat tin hieu OK và thay đổi label tương ứng
          
                self.ui.label_ok_4cam.setStyleSheet(f"background: #47ff4d;")
                self.ui.label_ng_4cam.setStyleSheet(f"background: #c6c6c6;")
        
    def process_queue_4cam_each_camera(self,image, image_binary, real, result, mode=0): # 4 Cam sau khi lấy được ảnh từng 
                                                                                        #   cam sẽ về đây để xử lý
        image_to_draw = image.copy()
        bit=0
        image_binary = cv2.resize(image_binary, (image.shape[1], image.shape[0]))
        # Tìm contours từ ảnh nhị phân
        contours, _ = cv2.findContours(image_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        ## Ngưỡng diện tích tối thiểu để lọc các vùng nhỏ
        # Duyệt qua các contours và vẽ những contour có diện tích >= min_area
        for contour in contours:
            area = cv2.contourArea(contour)
            if area >= self.value_4cam[0]:
                # Vẽ contour màu đỏ (BGR: (0, 0, 255)) với độ dày 2
                cv2.drawContours(image_to_draw, [contour], -1, (0, 0, 255), 2)
                bit=1
        if bit==0: # OK
            bit= 1
        else:      # NG
            bit= 2
        # Cập nhập lên GUI
        UI_of_main_gui.show_image_3chanel(self, image_to_draw.copy(), real)
        UI_of_main_gui.show_image_3chanel(self, image_binary.copy(), result)
        return image_to_draw.copy(),[bit,mode]

    def process_queue_4cam_cam2(self, *args, **kwargs):# Hàm dành riêng cho cam 2 nhưng cũng là phần xử lý tín hiệu luôn khi tổng hợp giá trị của 4 Cam
        while True:
            time.sleep(0.001)
            try:
                if self.running==True:
                    ## 4 Cam
                    name_special=''
                    top_image=None
                    bottom_image=None
                    # Khi nào cả 4 cam xử lý xong mới chạy được đoạn xuất tín hiệu này
                    if self.mode_cam2[1]==1 and self.mode_cam3[1]==1 and self.mode_cam4[1]==1 and self.mode_cam5[1]==1: # Đủ tín hiệu
                        self.result_output_4cam=0
                        
                        self.mode_cam2[1]=0
                        self.mode_cam3[1]=0
                        self.mode_cam4[1]=0
                        self.mode_cam5[1]=0

                        # Ghép ảnh để hiển thị lên View
                        top_image = np.hstack((self.real_image_4cam[0], self.real_image_4cam[1]))
                        bottom_image  = np.hstack((self.real_image_4cam[2], self.real_image_4cam[3]))
                        final_img = np.vstack((top_image, bottom_image))
                        UI_of_main_gui.show_image_3chanel(self, final_img, self.ui.show_pic_cam_4cam_view)

                        # Xuất tín hiệu
                        if self.mode_cam2[0]==1 and self.mode_cam3[0]==1 and self.mode_cam4[0]==1 and self.mode_cam5[0]==1: # Xuat tin hieu OK
                            self.mode_cam2[0]=0
                            self.mode_cam3[0]=0
                            self.mode_cam4[0]=0
                            self.mode_cam5[0]=0

                            self.ui.label_ok_4cam.setStyleSheet(f"background: #47ff4d;")
                            self.ui.label_ng_4cam.setStyleSheet(f"background: #c6c6c6;")

                            self.mode_output_2.value=1
                            self.result_output_4cam = True

                        else:
                            self.mode_cam2[0]=0
                            self.mode_cam3[0]=0
                            self.mode_cam4[0]=0
                            self.mode_cam5[0]=0
                            self.ui.label_ok_4cam.setStyleSheet(f"background: #c6c6c6;")
                            self.ui.label_ng_4cam.setStyleSheet(f"background: #ff0772;")

                            name_special= UI_of_main_gui.give_name_special(self)

                            # Save picture NG
                            self.save_data_into_database_4cam(self.real_image_4cam[0], self.vitrual_image_4cam[0], 2, name_special)
                            self.save_data_into_database_4cam(self.real_image_4cam[1], self.vitrual_image_4cam[1], 3, name_special)
                            self.save_data_into_database_4cam(self.real_image_4cam[2], self.vitrual_image_4cam[2], 4, name_special)
                            self.save_data_into_database_4cam(self.real_image_4cam[3], self.vitrual_image_4cam[3], 5, name_special)
                            
                            self.mode_output_2.value=2
                            self.result_output_4cam = False
                        

                        self.value_const_production_new= Cam_1.check_value_line_edit_production(self)
                        if self.value_const_production_new != self.value_const_production:
                            self.value_const_production_new = self.value_const_production
                            self.ui.lineEdit.setText(str(self.value_const_production))

                        # Tinh toan NG va OK
                        if len(self.result_output_cam1)>0:
                            if self.result_output_cam1.popleft()== True and self.result_output_4cam == True:
                                self.value_ok_production= self.value_ok_production+ self.value_const_production
                                
                                # Xuất tín hiệu label OK sáng lên ở View
                                self.ui.label_ok_view.setStyleSheet(f"background: #47ff4d;")
                                self.ui.label_ng_view.setStyleSheet(f"background: #c6c6c6;")

                            else:
                                self.value_ng_production= self.value_ng_production+ self.value_const_production

                                # Xuất tín hiệu label NG sáng lên ở View
                                self.ui.label_ok_view.setStyleSheet(f"background: #c6c6c6;")
                                self.ui.label_ng_view.setStyleSheet(f"background: #ff0772;")

                        self.count_4cam=self.count_4cam+1
                        print(f"Tong 4 cam chup duoc {self.count_4cam}")

                        self.update_sum_ok_ng_production()
                        self.update_value_production()

                        gc.collect()

                        self.real_image_4cam.clear()
                        self.vitrual_image_4cam.clear()
                    
                    ## Cam 2
                    if not self.queue_AI_cam2.empty():
                        self.image_cam2_4cam= self.queue_AI_cam2.get()
                        self.image_binary_cam2_4cam= self.queue_AI_cam2.get()
                        
                        # Lấy mẫu thì mở chúng ra để lấy mẫu
                        ## Remember resize binary image to original size of original image (==image_cam2_4cam)
                        ## Save with self.save_NG_to_train()

                        #================================
                        image, self.mode_cam2=self.process_queue_4cam_each_camera(self.image_cam2_4cam, self.image_binary_cam2_4cam,
                                                            self.ui.show_pic_real_1_4cam,self.ui.show_pic_result_1_4cam,1)

                        self.real_image_4cam.append(image)
                        self.vitrual_image_4cam.append(self.image_cam2_4cam.copy())
                    
            except (OSError, ValueError) as e:
                print(f"Queue cam2 error: {e}")
                sys.exit()

    def process_queue_4cam_cam3(self, *args, **kwargs):
        while True:
            time.sleep(0.001)
            if self.running==True:
                try:
                    ## Cam 3
                    if not self.queue_AI_cam3.empty():
                        self.image_cam3_4cam= self.queue_AI_cam3.get()
                        self.image_binary_cam3_4cam= self.queue_AI_cam3.get()

                        ## Save with self.save_NG_to_train()
                        #================================
                        image, self.mode_cam3=self.process_queue_4cam_each_camera(self.image_cam3_4cam, self.image_binary_cam3_4cam,
                                                            self.ui.show_pic_real_2_4cam,self.ui.show_pic_result_2_4cam,1)

                        self.real_image_4cam.append(image)
                        self.vitrual_image_4cam.append(self.image_cam3_4cam.copy())
                except (OSError, ValueError) as e:
                    print(f"Queue cam3 error: {e}")
    
    def process_queue_4cam_cam4(self, *args, **kwargs):
        while True:
            time.sleep(0.001)
            if self.running==True:
                try:
                    ## Cam 4
                    if not self.queue_AI_cam4.empty():

                        self.image_cam4_4cam= self.queue_AI_cam4.get()
                        self.image_binary_cam4_4cam= self.queue_AI_cam4.get()

                        ## Save with self.save_NG_to_train()
                        #================================
                        image, self.mode_cam4=self.process_queue_4cam_each_camera(self.image_cam4_4cam, self.image_binary_cam4_4cam,
                                                            self.ui.show_pic_real_3_4cam,self.ui.show_pic_result_3_4cam,1)
                        
                        self.real_image_4cam.append(image)
                        self.vitrual_image_4cam.append(self.image_cam4_4cam.copy())
                        
                except (OSError, ValueError) as e:
                    print(f"Queue cam4 error: {e}")
    
    def process_queue_4cam_cam5(self, *args, **kwargs):
        while True:
            time.sleep(0.001)
            if self.running==True:
                try:
                    ## Cam 5
                    if not self.queue_AI_cam5.empty():

                        self.image_cam5_4cam= self.queue_AI_cam5.get()
                        self.image_binary_cam5_4cam= self.queue_AI_cam5.get()
                        
                        ## Save with self.save_NG_to_train()
                        #================================
                        image, self.mode_cam5=self.process_queue_4cam_each_camera(self.image_cam5_4cam, self.image_binary_cam5_4cam,
                                                            self.ui.show_pic_real_4_4cam,self.ui.show_pic_result_4_4cam,1)

                        self.real_image_4cam.append(image)
                        self.vitrual_image_4cam.append(self.image_cam5_4cam.copy())

                except (OSError, ValueError) as e:
                    print(f"Queue cam4 error: {e}")
    
    def save_NG_to_train(self, image, index):
        # Láy đường dẫn
        link = os.path.join(self.current_file_path, "data_cam_group", f"cam{index}_ok")  #ok
        link = os.path.join(self.current_file_path, "data_cam_group", f"cam{index}_ng")  #ng

        name, link_path= UI_of_main_gui.give_name_file(self,link)
        link_path = os.path.join(self.current_file_path, "data_cam_group", f"cam{index}_ok", f"cam{index}_ok_"+name) #ok
        link_path = os.path.join(self.current_file_path, "data_cam_group", f"cam{index}_ng", f"cam{index}_ng_"+name) #ng
        cv2.imwrite(link_path, image)

    def process_queue_cam1(self, *args, **kwargs): # Process xử lý cho Cam 1
        while True:
            time.sleep(0.00001)
            if self.running==True:
                if not self.current_queue_cam1.empty():
                    time_start= time.time()

                    image= self.current_queue_cam1.get()
                    if self.mode_pic_cam1.value==1 and self.file_count_calib <7: # Hàm Calib
                        image_path = os.path.join(self.current_file_path, "data_calib", f"{self.file_count_calib+1}.png")
                        image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        cv2.imwrite(image_path,image)
                        Calib.check_file_in_folder(self)

                    elif self.mode_pic_cam1.value==2:# Hàm lấy mẫu
                        # Phải Calib trước
                        image = self.frame_calibrate.undistortImage(image.copy()) 
                        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                        link = os.path.join(self.current_file_path, "picture", "sample_cam1.png")
                        cv2.imwrite(link,image)
                        self.sample.reset()

                    else:# Hàm xử lý chính với cam 1
                        self.mode_cam1=0 # Bit NG cam 1

                        # Qua lớp calib
                        image = self.frame_calibrate.undistortImage(image.copy())
                        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        self.image_cam1=image.copy()

                        self.image_sample_cam1=cv2.imread(os.path.join(self.current_file_path, "picture", "saved_sample.png"))
                        self.time_start=time.time()

                        # Temp-matching hình ảnh nguyên bản được vẽ lên và hình ảnh nhỏ của vùng được scale
                        # Trả lại ảnh được vẽ box với đối tượng xac định và ảnh cắt ra so với ảnh Sample
                        self.image_process, self.image_matching_process=self.template_matching(self.image_cam1.copy(),self.image_sample_cam1.copy())
                        if self.image_process is not None and self.image_matching_process is not None:
                            # cv2.imwrite('data_check/test_cam1.png',self.image_matching_process)
                            UI_of_main_gui.show_image_3chanel(self,self.image_process,self.ui.show_pic_cam_cam1)
                            self.process_cam_1(self.value_saved_cam1)
                        else: 
                            UI_of_main_gui.show_image_3chanel(self,self.image_cam1,self.ui.show_pic_cam_cam1)
                            
                            # Khi thấy cả frame ảnh lớn là biết không matching được
                            UI_of_main_gui.show_image_3chanel(self,self.image_cam1,self.ui.show_pic_cam_cam1_view)

                            # Clear các label đang hiện hình ảnh trước đó
                            self.ui.show_pic_real_cam1.clear()
                            self.ui.show_pic_thread_cam1.clear()
                            self.ui.show_pic_virtual_cam1.clear()

                        if self.mode_cam1==0: #NG
                            self.ui.label_ok_cam1.setStyleSheet(f"background: #c6c6c6;")
                            self.ui.label_ng_cam1.setStyleSheet(f"background: #ff0772;")
                            self.mode_output_1.value=2
                            self.result_output_cam1.append(False)
                        else:                 #OK
                            self.ui.label_ok_cam1.setStyleSheet(f"background: #47ff4d;")
                            self.ui.label_ng_cam1.setStyleSheet(f"background: #c6c6c6;")
                            self.mode_output_1.value=1
                            self.result_output_cam1.append(True)
                        self.count_cam1=self.count_cam1+1
                        print(f"Tong cam 1 chup duoc {self.count_cam1}") # Giá trị để debug

                        ## Thống nhất giá trị của QSlider với cam 1 vì có 2 giá trị là now và đã lưu
                        # Now: là giá trị tạm thời nếu muốn lưu lại giá trị đó thì phải Save
                        # Đã lưu và giá trị mình muốn xử lý
                        Cam_1.undo_data(self)
                    
                    # In Circle time
                    # print((time.time()-time_start))

    def process_cam_1(self, value):
        #   Gồm 2 ảnh: ảnh được vẽ box với đối tượng xac định và ảnh cắt ra so với ảnh Sample
        if self.image_process is not None and self.image_matching_process is not None:

            image_matching_process_burred=cv2.blur(self.image_matching_process.copy(),(3,3))
            # Hình ảnh cắt ra của hình chữ nhật đó
            # image_matching_process_drawed=image_matching_process_burred.copy()
            picture_drawed=0
            contours=0
            area=0

            image_process=cv2.convertScaleAbs(image_matching_process_burred.copy(), alpha = value[7], beta = value[6])
            image_matching_process_drawed=image_process.copy() # thay doi thu
            hsv = cv2.cvtColor(image_process.copy(), cv2.COLOR_BGR2HSV)

            # Tạo mask bằng cách phân ngưỡng HSV
            upper_hsv= value[0],value[1], value[2]
            lower_hsv= value[3],value[4], value[5]
        
            mask = cv2.inRange(hsv, (lower_hsv), (upper_hsv))
            mask = cv2.bitwise_not(mask)
            kernel = np.ones((3, 3), np.uint8)
            mask = cv2.dilate(mask, kernel, iterations=1)
            # Tìm contours
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
          
            if contours:
                # Tìm contour lớn nhất
                largest_contour = max(contours, key=cv2.contourArea)
                area            = cv2.contourArea(largest_contour)
                self.ui.show_value_area_cam1.setText(str(int(area)))
                if value[10]-5000<int(area)<value[10]+6000: # Ngưỡng phần trắng lớn nhất nằm bên trong trong giới hạn cho phép
                    # Vẽ bounding box thẳng
                    x, y, w, h = cv2.boundingRect(largest_contour)
                    padding = 15
                    y1, y2 = max(0, y - padding), min(mask.shape[0], y + h + padding)
                    x1, x2 = max(0, x - padding), min(mask.shape[1], x + w + padding)
                    # cropped_image = mask[y:y+h, x:x+w]
                    # Cắt ảnh với vùng mở rộng
                    cropped_image = mask[y1:y2, x1:x2]
                    # cv2.imwrite("data_check/test_circle.png", cropped_image)
                    picture_drawed=image_matching_process_drawed[y1:y2, x1:x2]

                    # Chương trình check bavia
                    image_insert= self.detect_bavia_by_angle(picture_drawed, cropped_image, value)
                    image_matching_process_drawed[y1:y2, x1:x2]=image_insert
                    # cv2.rectangle(image_matching_process_drawed, (x, y), (x + w, y + h), (0, 0, 255), 2)
            
                    UI_of_main_gui.show_image_3chanel(self,image_matching_process_drawed,self.ui.show_pic_real_cam1)
                    UI_of_main_gui.show_image_3chanel(self,mask,self.ui.show_pic_thread_cam1)

                else: 
                    UI_of_main_gui.show_image_3chanel(self,image_matching_process_drawed,self.ui.show_pic_real_cam1)
                    UI_of_main_gui.show_image_3chanel(self,mask,self.ui.show_pic_thread_cam1)

                    # Xuất ra màn hình View
                    UI_of_main_gui.show_image_3chanel(self,image_matching_process_drawed,self.ui.show_pic_cam_cam1_view)

                    mask_save = np.zeros_like(image_process.copy())
                    self.save_data_into_database_cam1(image_process.copy(), mask_save)
                    self.ui.show_pic_virtual_cam1.clear()

            # In ra Circle Time
            self.time_end=time.time()
            # print(f'FPS all of process cam 1: {(1/(self.time_end-self.time_start)):.3f}')

    def check_bavia(self,image , image_gray, value):# Chương trình check bavia cũ, dựa vào mật độ
                                                    #   Gaussin và trung bình từ tâm ra đến các cạnh
        start=time.time()
        nan_count=0
        # Tìm contour lớn nhất (hình tròn)
        contours, _ = cv2.findContours(image_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            print("Không tìm thấy hình tròn trong ảnh.")
            return None
    
        largest_contour = max(contours, key=cv2.contourArea)

        # Xác định tâm bằng bounding box của contour
        x, y, w, h = cv2.boundingRect(largest_contour)
        cx, cy = int(x + w / 2), int(y + h / 2)  # Tâm của bounding box

        # Tạo mask từ contour
        mask = np.zeros_like(image_gray.copy())
        cv2.drawContours(mask, [largest_contour], -1, 255, thickness=-1)

        # Tạo ảnh màu để vẽ kết quả
        output_virtual = cv2.cvtColor(mask.copy(), cv2.COLOR_GRAY2BGR)

        # **BƯỚC 1: Tạo bảng góc trước**
        angles_ref = np.linspace(0, 360, 360, endpoint=False)  # 360 giá trị từ 0° đến 359°

        # **BƯỚC 2: Tính toán nhanh góc & khoảng cách**
        contour_points = largest_contour[:, 0, :]  # Lấy danh sách các điểm biên

        # Tính khoảng cách từ tâm đến từng điểm biên
        dx = contour_points[:, 0] - cx
        dy = contour_points[:, 1] - cy
        distances = np.sqrt(dx**2 + dy**2)

        # Tính góc của từng điểm so với tâm
        angles = np.arctan2(dy, dx) * 180 / np.pi  # Chuyển đổi sang độ
        angles = np.mod(angles, 360)  # Đảm bảo góc trong khoảng 0-360

        # **BƯỚC 3: Ánh xạ khoảng cách vào mảng `r_list`**
        r_list = np.full(360, np.nan)

        # Tìm góc gần nhất trong `angles_ref` bằng broadcasting
        angle_indices = np.abs(angles[:, None] - angles_ref).argmin(axis=1)

        # Gán khoảng cách vào r_list
        for i in range(len(angle_indices)):
            r_list[angle_indices[i]] = distances[i]
        nan_count = np.isnan(r_list).sum()

        # **Nội suy giá trị NaN để làm mượt**
        valid_r = r_list[~np.isnan(r_list)]  # Lọc bỏ giá trị NaN

        # Kiểm tra nếu valid_r rỗng
        if valid_r.size == 0:
            print("⚠️ Không có giá trị hợp lệ trong r_list! Đặt mặc định r = 0")
            valid_r = np.array([0])  # Tránh lỗi khi tính mean

        for i in range(len(r_list)):
            if np.isnan(r_list[i]):
                start_idx = max(0, i - 5)
                end_idx = min(len(valid_r), i + 5)

                # Nếu đoạn cần lấy trung bình vẫn rỗng, thì thay thế bằng giá trị mặc định
                if valid_r[start_idx:end_idx].size == 0:
                    r_list[i] = 0  # Giá trị mặc định khi không có dữ liệu hợp lệ
                else:
                    r_list[i] = np.mean(valid_r[start_idx:end_idx])  # Trung bình cục bộ
        
        valid_r = np.sort(valid_r)

        # **Tính bán kính trung bình từ 100 giá trị nhỏ nhất**
        first_120 = np.random.choice(valid_r[:100], min(60, len(valid_r[:100])), replace=False)  # Lấy ngẫu nhiên 20 giá trị từ giữa
        middle_50 = np.random.choice(valid_r[80:300], min(50, len(valid_r[100:200])), replace=False)  # Lấy ngẫu nhiên 50 giá trị từ giữa
        # last_10 = np.random.choice(valid_r[300:], min(15, len(valid_r[300:])), replace=False)  # Lấy ngẫu nhiên 50 giá trị từ giữa

        # Gộp tất cả vào một danh sách
        selected_values = np.concatenate([ first_120,middle_50])

        # Tính r_mean
        r_mean = np.median(np.sort(selected_values))

        # Debug số lượng góc có giá trị hợp lệ
        # print(f"Số góc có giá trị hợp lệ: {np.count_nonzero(~np.isnan(r_list))} / 360")

        # Nội suy nếu còn thiếu
        valid_indices = np.where(~np.isnan(r_list))[0]
        valid_r_values = r_list[valid_indices]
        full_indices = np.arange(360)
        r_list = np.interp(full_indices, valid_indices, valid_r_values)

        # **Vẽ các đường tia**
        count_red = 0
        for angle in range(0, 360, 1):  # Giảm mật độ tia (mỗi 2 độ)
            theta = np.deg2rad(angle)
            r = r_list[angle]

            # Xác định màu sắc
            if value[9]< abs(r - r_mean):
                color = (0, 0, 255)  # Đỏ nếu bất thường
                count_red += 1  
            else:
                color = (0, 255, 0)  # Xanh nếu ổn

            # Xác định điểm kết thúc
            x_end, y_end = int(cx + r * np.cos(theta)), int(cy + r * np.sin(theta))

            # Vẽ đường tia
            cv2.line(output_virtual, (cx, cy), (x_end, y_end), color, 1)
            # if color==(0, 0, 255):
                # cv2.line(image, (cx, cy), (x_end, y_end), color, 1)

        self.ui.show_value_now_cam1.setText(f'Điểm NG phát hiện: {count_red}')
        # print(f'Gia tri NG la{count_red}')
        # print(f'Gia tri Nan la{nan_count}')

        if (count_red) > value[8]: #NG
            
            self.ui.label_ok_cam1.setStyleSheet(f"background: #c6c6c6;")
            self.ui.label_ng_cam1.setStyleSheet(f"background: #ff0772;")
            self.save_data_into_database_cam1(image.copy(), output_virtual.copy())
        else: # OK
            self.ui.label_ok_cam1.setStyleSheet(f"background: #47ff4d;")
            self.ui.label_ng_cam1.setStyleSheet(f"background: #c6c6c6;")

        cv2.circle(image, (cx, cy), 5, (255, 0, 0), -1)
        UI_of_main_gui.show_image_3chanel(self,output_virtual,self.ui.show_pic_virtual_cam1)
        self.mode_output_1.value=2
        fps= (1/(time.time()-start))
        # print(f'Gias tri fps la: {fps:.3f}')
        return image

    def detect_bavia_by_angle(self,image , image_gray, value):# Chương trình check bavia mới, ý tưởng dựa trên tập hơp các cạnh   
                                                                # liền kề và chúng không được tạo một góc vượt quá ngưỡng cho phép
        start = time.time()

        # Resize nếu cần: lý do ảnh binary và ảnh thực tế sai kích thước cho bị cắt lượt bớt nên kích thước khác nhau
        if image_gray.shape[:2] != image.shape[:2]:
            image_gray = cv2.resize(image_gray, (image.shape[1], image.shape[0]))

        # Tìm contour lớn nhất
        contours, _ = cv2.findContours(image_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        largest_contour = max(contours, key=cv2.contourArea)

        # Tạo mask từ contour
        mask = np.zeros_like(image_gray.copy())
        cv2.drawContours(mask, [largest_contour], -1, 255, thickness=-1)

        # Đảo ngược màu của mask
        mask = cv2.bitwise_not(mask)
        # cv2.imshow("Detect", mask)
        # cv2.waitKey(0)

        # Tạo ảnh màu để vẽ kết quả
        output_virtual = image.copy()

        # Tìm contour có diện tích lớn nhất
        contour = largest_contour[:, 0, :].astype(np.float32)  # (N, 2) và float32 cho nhanh
        if len(contour) < 5: # bắt buộc phải có contour vì đã lọc ảnh phải tương thích với ảnh matching của Sample rồi 
                            #   và cũng không được nhiễu quá nhiều thường hàm này dùng để biết khi nào đĩa xoay tròn bị bẩn
            # print("Contour quá nhỏ.")
            return image

        step = max(1, len(contour) // 180)
        idx = np.arange(step, len(contour) - step, step)
        p0 = contour[idx - step]

        p1 = contour[idx]
        p2 = contour[idx + step]

        # Vector hóa
        v1 = p1 - p0
        v2 = p2 - p1

        v1_norm = np.linalg.norm(v1, axis=1, keepdims=True)
        v2_norm = np.linalg.norm(v2, axis=1, keepdims=True)

        # Tránh chia 0
        v1_norm = np.maximum(v1_norm, 1e-8)
        v2_norm = np.maximum(v2_norm, 1e-8)

        unit_v1 = v1 / v1_norm
        unit_v2 = v2 / v2_norm

        dot_products = np.sum(unit_v1 * unit_v2, axis=1)
        dot_products = np.clip(dot_products, -1.0, 1.0)
        angles_deg = np.degrees(np.arccos(dot_products))

        # Tìm các điểm nghi ngờ
        spike_mask = angles_deg > value[9]
        spike_points = p1[spike_mask].astype(int)

        spike_lines = zip(p1[spike_mask], p2[spike_mask])  # Vẽ từ p1 đến p2

        self.ui.show_value_now_cam1.setText(f'Điểm NG phát hiện: {len(spike_points)}')

        if len(spike_points) > value[8]: #NG
            # cv2.drawContours(output_virtual, [largest_contour], -1, (0, 0, 255), 3)
            # Vẽ 1 lần duy nhất
            for pt1, pt2 in spike_lines:
                pt1 = tuple(pt1.astype(int))
                pt2 = tuple(pt2.astype(int))
                cv2.circle(output_virtual, pt1, 3, (0, 0, 255), -1)
                cv2.line(output_virtual, pt1, pt2, (0, 0, 255), 2)  # vẽ line đỏ
            self.save_data_into_database_cam1(image.copy(), output_virtual.copy())
        else: # OK
            self.mode_cam1=1
            cv2.drawContours(output_virtual, [largest_contour], -1, (0, 255, 0), 3)
            
        UI_of_main_gui.show_image_3chanel(self,output_virtual,self.ui.show_pic_virtual_cam1)

        # Xuất ra màn hình View
        UI_of_main_gui.show_image_3chanel(self,output_virtual,self.ui.show_pic_cam_cam1_view)

        fps= (1/(time.time()-start))
        # print(f'FPS process bavia cam1: {fps:.3f}')
        return image
 
    def save_data_into_database_cam1(self,image_real, image_thread): # Lưu vào file database với các giá trị Cam 1
        # print(' Đưa lưu lại NG và đưa vào database')
        if not os.path.exists(self.real_path_ng_cam1):
            os.makedirs(self.real_path_ng_cam1)

        if not os.path.exists(self.virtual_path_ng_cam1):
            os.makedirs(self.virtual_path_ng_cam1)

        # Lấy tên cho ảnh nào
        name_real   , link_real     = UI_of_main_gui.give_name_file(self,self.real_path_ng_cam1 )
        name_virtual, link_vitrual  = UI_of_main_gui.give_name_file(self,self.virtual_path_ng_cam1)

        cv2.imwrite(link_real, image_real)
        cv2.imwrite(link_vitrual, image_thread)
        self.save_to_database(self.database[0], name_real)

    def save_data_into_database_4cam(self, image_real, image_thread, index=0, name_special=''):# Lưu vào file database với các giá trị 4 Cam
        # print(f' Đưa lưu lại NG cam {index} và đưa vào 2 database')
        link_real_path_ng4cam=None
        link_virtual_ng4cam=None

        # Dùng để lưu ảnh thật
        if not os.path.exists(self.real_path_ng_4cam):
            os.makedirs(self.real_path_ng_4cam)
        link_real_path_ng4cam= os.path.join(self.real_path_ng_4cam, f"cam{index}")
        if not os.path.exists(link_real_path_ng4cam):
            os.makedirs(link_real_path_ng4cam)

        # Dùng để lưu ảnh ảo,  đã thay là ảnh thật có khoanh NG bằng nét màu đỏ
        if not os.path.exists(self.virtual_path_ng_4cam):
            os.makedirs(self.virtual_path_ng_4cam)
        link_virtual_ng4cam= os.path.join(self.virtual_path_ng_4cam, f"cam{index}")
        if not os.path.exists(link_virtual_ng4cam):
            os.makedirs(link_virtual_ng4cam)

        # Lấy tên cho ảnh nào
        link_real     = os.path.join(link_real_path_ng4cam,name_special)
        link_vitrual  = os.path.join(link_virtual_ng4cam,name_special)

        cv2.imwrite(link_real, image_real)
        cv2.imwrite(link_vitrual, image_thread)

        if index==2:# Vì đường dẫn chỉ cần lưu 1 cái thôi chứ không cần đường dẫn của cả 4 giá trị
            self.save_to_database(self.database[1], name_special)

    def template_matching(self, image, sample):
        image_draw=None
        matched_region=None

        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)

        # Tạo mask để loại bỏ nền đen
        _, mask = cv2.threshold(gray_template, 50, 255, cv2.THRESH_BINARY)

        # Matching sử dụng template matching
        result = cv2.matchTemplate(gray_img, gray_template, cv2.TM_CCOEFF_NORMED, mask=mask)

        # Tìm vị trí matching tốt nhất
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Kiểm tra nếu matching trên 80%
        threshold = 0.8 

        # print(f'Ngưỡng hiện tại: {max_val}')
        if max_val >= threshold:

            # Vẽ hình chữ nhật quanh vùng matching
            h, w = gray_template.shape
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            image_draw=image.copy()
            cv2.rectangle(image_draw, top_left, bottom_right, (0, 255, 0), 2)

            # Cắt ảnh vùng matching
            matched_region = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        
        # center_x = (top_left[0] + bottom_right[0]) // 2
        # center_y = (top_left[1] + bottom_right[1]) // 2
        # self.center_cam1=(center_x,center_y)

        return image_draw, matched_region

    def auto_calib(self, *args, **kwargs): # Hàm tự động chạy Calib
        if self.file_count_calib>=5:
            json_path = os.path.join(self.current_file_path, "data_calib", "calib_camera.json")

            path_folder = os.path.join(self.current_file_path, "data_calib")
            bmp_files = os.path.join(path_folder, "*.png")  # Lấy tất cả file bmp

            self.frame_calibrate = FrameCalibrate(json_path)

            image,ret= self.frame_calibrate.calibrateCameraMatrix(
            bmp_files, 
            (23, 19), 
            3, True)
            if ret !=0:
                UI_of_main_gui.show_image_3chanel(self, image, self.ui.show_pic_calib_calib)
                self.current_label.setStyleSheet(f"background-color: green;")

            else:
                self.current_label.setText(f"Không calib được")
                self.current_label.setStyleSheet(f"background-color: red;")

    def save_to_database(self, db_name, filename): # Hàm truyền vào database của SQL Lite với cam 1 
        # print('Chuyển đường dẫn vào database')
        db_path = os.path.join(self.current_file_path, "data_txt", db_name)

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO images (filename) VALUES (?)", (filename,))
            conn.commit()
            # print(f"✅ Đã lưu {filename} vào {db_name}")
        except sqlite3.IntegrityError:
            print(f"⚠️ File {filename} đã tồn tại trong {db_name}")
        finally:
            conn.close()  # Đóng kết nối sau khi hoàn thành

    def get_recent_filenames(self, db_name, limit=100):
        """Lấy 100 file mới nhất từ database cụ thể, mở kết nối mới để tránh lỗi thread"""
        db_path = os.path.join(self.current_file_path, "data_txt", db_name)
        try:
            # Mở kết nối mới trong từng thread
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Truy vấn 100 file gần nhất
            cursor.execute("SELECT filename FROM images ORDER BY id DESC LIMIT ?", (limit,))
            filenames = [row[0] for row in cursor.fetchall()]

        except sqlite3.Error as e:
            print(f"❌ Lỗi SQLite ({db_name}): {e}")
            filenames = []

        finally:
            conn.close()  # Đóng kết nối sau khi hoàn thành

        return filenames
    
    def create_or_check_database(self, *args, **kwargs):
        self.db_connections = {}  # Lưu kết nối để dễ dùng sau này
        for db_name in self.database:
            db_path = os.path.join(self.current_file_path, "data_txt", db_name)
            # print("Database Path:", db_path)  # Kiểm tra đường dẫn
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Tạo bảng nếu chưa tồn tại
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS images (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT UNIQUE
                )
            ''')
            conn.commit()
        
            # Lưu kết nối
            self.db_connections[db_name] = conn
        # nếu có rồi thì nó sẽ không xóa dữ liệu còn tồn tại


        self.db_prodcuction = {}  # Lưu kết nối để dễ dùng sau này
        for db_name in self.database_production:

            db_path = os.path.join(self.current_file_path, "data_txt", db_name)
            # print("Database Path:", db_path)  # Kiểm tra đường dẫn
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Tạo bảng nếu chưa tồn tại
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS my_dataset (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    start_day TEXT,
                    end_day TEXT,
                    count_ok INTEGER,
                    count_ng INTEGER,
                    count_sum INTEGER,
                    ratio REAL
                )
            ''')
            conn.commit()
        
            # Lưu kết nối
            self.db_prodcuction[db_name] = conn
        # nếu có rồi thì nó sẽ không xóa dữ liệu còn tồn tại

    def close_all_databases(self, *args, **kwargs):
        """Đóng tất cả kết nối database khi thoát chương trình"""
        for db_name, conn in self.db_connections.items():
            conn.close()
            print(f"🔌 Đã đóng {db_name}")
        self.db_connections.clear()  # Xóa danh sách kết nối

        for db_name, conn in self.db_prodcuction.items():
            conn.close()
            print(f"🔌 Đã đóng {db_name}")
        self.db_prodcuction.clear()  # Xóa danh sách kết nối
    
    def check_month_forth(self, *args, **kwargs):
        # Đọc xem hiện tại là tháng nào ở file txt nếu có thay đổi thì cập nhập liền 
        path_folder=os.path.join(self.current_file_path,'data_txt','moth_forth.txt')
        value_year_forth=self.read_file(path_folder)
        value_year_forth= self.exchange_data(value_year_forth)
        
        year_forth= value_year_forth[0]
        link_databases=['data_cam1.db','data_4cam.db']

        if int(self.month_now) != year_forth:
            for link_database in link_databases:
                db_path = os.path.join(self.current_file_path, "data_txt", link_database)
                if os.path.exists(db_path):
                    os.remove(db_path)
            
            # Update month now
            path_folder=os.path.join(self.current_file_path,'data_txt','moth_forth.txt')
            data=open(path_folder, "w")
            data_month_now = [ str(int(self.month_now))+"\n"
                        ]
            
            data.writelines(data_month_now)
            data.close()

    def update_end_day_production(self, *args, **kwargs):
        db_path = os.path.join(self.current_file_path, "data_txt", self.database_production[0])

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        if not conn:
            # print(f"Không tìm thấy kết nối DB: {self.database_production[0]}")
            return
        
        now = datetime.now().strftime("%Y-%m-%d")
        cursor.execute('''
            UPDATE my_dataset
            SET end_day = ?
            WHERE id = (SELECT MAX(id) FROM my_dataset)
        ''', (now,))

        conn.commit()

    def update_sum_ok_ng_production(self, *args, **kwargs):
        db_path = os.path.join(self.current_file_path, "data_txt", self.database_production[0])

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        count_ok = self.value_ok_production
        count_ng = self.value_ng_production
        count_sum = count_ok + count_ng
        ratio =   round(count_ok / count_sum, 3) if count_sum > 0 else 0.0

        if not conn:
            # print(f"Không tìm thấy kết nối DB: {self.database_production[0]}")
            return
        
        count_sum = count_ok + count_ng
        ratio = count_ok / count_sum if count_sum > 0 else 0.0

        cursor.execute('''
            UPDATE my_dataset
            SET count_ok = ?, count_ng = ?, count_sum = ?, ratio = ?
            WHERE id = (SELECT MAX(id) FROM my_dataset)
        ''', (count_ok, count_ng, count_sum, f"{ratio:.3f}"))

        conn.commit()
    
    def insert_new_data_into_database_production(self, *args, **kwargs): # Hàm ở phần Sản lượng khi thêm một giá trị mới muốn theo dõi
        self.value_const_production_new= Cam_1.check_value_line_edit_production(self)
        if self.value_const_production_new != self.value_const_production:
            self.value_const_production_new = self.value_const_production
            self.ui.lineEdit.setText(str(self.value_const_production))

        self.value_ok_production= 0
        self.value_ng_production= 0
        self.end_date_production= datetime.now()
        self.update_production()
        self.save_value_production()

        start_day = self.end_date_production.strftime("%Y-%m-%d")   # start day === end day 
        end_day = datetime.now().strftime("%Y-%m-%d")     # end day ==start day
        count_ok = self.value_ok_production
        count_ng = self.value_ng_production
        count_sum = count_ok + count_ng
        ratio =   round(count_ok / count_sum, 3) if count_sum > 0 else 0.0

        db_path = os.path.join(self.current_file_path, "data_txt", self.database_production[0])

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO my_dataset (start_day, end_day, count_ok, count_ng, count_sum, ratio)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (start_day, end_day, count_ok, count_ng, count_sum, f"{ratio:.3f}"))

        conn.commit()
    
    def read_database_production(self,*args, **kwargs):
        db_path = os.path.join(self.current_file_path, "data_txt", self.database_production[0])
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        if not conn:
            print(f"Không tìm thấy DB: {db_path}")
            return []

        cursor = conn.cursor()
        cursor.execute('''
            SELECT start_day, end_day, count_ok, count_ng, count_sum, ratio
            FROM my_dataset
            ORDER BY id DESC
            LIMIT 20
        ''')
        rows = cursor.fetchall()
        # return rows[::-1]  # đảo ngược để dòng mới nhất nằm cuối bảng
        return rows  # đảo ngược để dòng mới nhất nằm cuối bảng

    def show_on_table(self, data):
        table = self.ui.data_output
        table.clearContents()
        table.setRowCount(len(data))
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(['Start Day', 'End Day', 'OK', 'NG', 'Sum', 'Ratio'])

        # Tắt đánh số dòng bên trái
        table.verticalHeader().setVisible(False)

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_idx, col_idx, item)

    
    def monitor_production(self, *args, **kwargs):
        data_xxx=None
        today = datetime.now()
        self.ui.show_to_date_output.setText('Đến ngày : ' + today.strftime("%Y-%m-%d"))

        self.ui.show_value_now_output.setText(f'Giá trị hiện tại:  {self.value_ok_production +self.value_ng_production}')
        self.ui.label_production_ok.setText(f'Giá trị OK:  {self.value_ok_production}')
        self.ui.label_production_ng.setText(f'Giá trị NG:  {self.value_ng_production}')

        data_xxx=self.read_database_production()
        self.show_on_table(data_xxx)

    def update_production(self, *args, **kwargs):
        self.value_const_production_new= Cam_1.check_value_line_edit_production(self)
        self.ui.lineEdit.setText(str(self.value_const_production_new))
    
    def save_value_production(self, *args, **kwargs):
        self.value_const_production= self.value_const_production_new
        self.update_value_production()

    def update_value_production(self, *args, **kwargs):
        # Đường dẫn file
        file_path = os.path.join(self.current_file_path,'data_txt','value_production.txt')

        # Ghi vào file
        with open(file_path, "w") as f:
            f.write(f"{self.value_const_production}\n")
            f.write(f"{self.value_ok_production}\n")
            f.write(f"{self.value_ng_production}\n")
            # f.write(f"{self.end_date_production.strftime('%Y-%m-%d')}\n")
            # f.write(f"{self.end_date_production}\n")
            f.write(f"{self.end_date_production.strftime('%Y-%m-%d')}\n")

    def init_production(self, *args, **kwargs):# Hàm khởi động khi chạy chương trình tính Sản lượng
        path_folder=os.path.join(self.current_file_path,'data_txt','value_production.txt')
        value=self.read_file(path_folder)

        for i, value in enumerate(value):
            if i==0:
                self.value_const_production= int(value)
            elif i==1:
                self.value_ok_production= int(value)
            elif i==2:
                self.value_ng_production= int(value)
            elif i==3:
                self.end_date_production= datetime.strptime(value.strip(), "%Y-%m-%d")
        
        self.ui.show_date_from_output.setText('Từ ngày : ' + self.end_date_production.strftime("%Y-%m-%d"))
        
        self.ui.lineEdit.setText(str(self.value_const_production))
        self.value_const_production_new= self.value_const_production

    def auto_check_and_create_folder_and_file_NG(self, *args, **kwargs):
        link=os.path.join(self.current_file_path, "data_NG")

        self.year_backup=[]
        self.month_backup=[]
        self.path_ng_save_today=None

        today=datetime.today()
        # Lấy thời điểm hiện tại
        self.day_now= today.day
        self.month_now= today.month
        self.year_now= today.year

        # Tao folder hien tai de su dung cho muc dich luu tru
        self.path_folder_year_now   = os.path.join(link,str(self.year_now))
        self.path_folder_today_ng_now_cam1   = os.path.join(self.path_folder_year_now ,str(self.month_now),'cam1')
        self.path_folder_today_ng_now_4cam   = os.path.join(self.path_folder_year_now ,str(self.month_now),'4cam')
        ## Nếu không có thì phải tạo
        if not os.path.exists(self.path_folder_today_ng_now_cam1):
            os.makedirs(self.path_folder_today_ng_now_cam1)

        if not os.path.exists(self.path_folder_today_ng_now_4cam):
            os.makedirs(self.path_folder_today_ng_now_4cam)

        ## Check lai folder voi muc dich chi co the chua duoc nhieu nhat 6 thang
        # check năm
        for year in os.listdir(link):
            self.year_backup.append(year)
        self.year_backup=sorted(self.year_backup)
        check_year_now=os.path.join(link, self.year_backup[-1])

        # Check tháng trong năm nhỏ nhất trong chuỗi
        for month in os.listdir(check_year_now):
            self.month_backup.append(month)
        self.month_backup=sorted(self.month_backup)

        if int(self.month_backup[-1])>=6:
            if len(self.month_backup)>6:
                for month in self.month_backup[0:-6]:
                    path_month_clear=os.path.join(check_year_now,month)

                    if os.path.exists(path_month_clear):
                        shutil.rmtree(path_month_clear)
            
            for year in self.year_backup[:-1]:
                path_year_to_clear=os.path.join(link, year)

                if os.path.exists(path_year_to_clear):
                    shutil.rmtree(path_year_to_clear)
        else:
            # số tháng còn có thể chứa lại bên kia là 
            month_cap=6-int(self.month_backup[-1])
            if len(self.year_backup) >= 2:
                path_year_old=os.path.join(link, self.year_backup[-2])
                for month in os.listdir(path_year_old):
                    # month=month
                    if int(month)<=(12-month_cap):
                        path_month_old_clear=os.path.join(path_year_old,month)
                        if os.path.exists(path_month_old_clear):
                            shutil.rmtree(path_month_old_clear)

    def monitor_month_change(self, *args, **kwargs): # Giám sát thay đổi giờ tháng năm theo thời gian sau 1 minute
        # Láy giá trị mong muốn ở hiện tại
        current_month = datetime.now().month
        current_day = datetime.now().day

        if current_day != self.day_now: # Nếu ngày thay đổi
            self.day_now= current_day
            self.update_end_day_production()

        if current_month != self.month_now:  # Nếu tháng thay đổi
            self.auto_check_and_create_folder_and_file_NG()
            self.check_month_forth()
            self.create_or_check_database()

    def popup_open(self, *args, **kwargs):
        self.screen_2=SubWindow(self)
        self.screen_2.adjustSize()

        # Lấy tọa độ gốc (global) của stackedWidget
        stacked_geo = self.ui.stackedWidget.geometry()
        stacked_pos = self.ui.stackedWidget.mapToGlobal(stacked_geo.topLeft())

        # Lấy kích thước của stackedWidget
        stacked_width = self.ui.stackedWidget.width()
        stacked_height = self.ui.stackedWidget.height()

        # Lấy kích thước thực tế của screen_2
        dialog_width = self.screen_2.width()
        dialog_height = self.screen_2.height()

        # Tính tọa độ để căn giữa screen_2 trong stackedWidget
        center_x = stacked_pos.x() + (stacked_width - dialog_width) // 2
        center_y = stacked_pos.y() + (stacked_height - dialog_height) // 2-100

        self.screen_2.move(center_x, center_y)  # Di chuyển đến vị trí căn giữa
        self.screen_2.show()

    def closeEvent(self, event):
        # Khi kết thúc chương trình thì phải lưu lại giá trị Sản lượng đang hiện có tất nhiên là mình cũng đã lưu liên tục
        #  phòng bị có vấn đề phát sinh lỗi
        self.update_value_production()

        # Đóng các database
        self.close_all_databases()
        self.mode_run_AI.flag=False # đưa cờ chạy AI tắt di
        self.process_AI.terminate()
        self.running=False # đưa cờ chạy 4 cam tắt đi
        print("Ngắt kết nối camera thoát chương trình")
        self.camera.close()
        gc.collect()
        event.accept()

class camera_Basler_multi:
    def __init__(self, pic_queue, pic_queue2, pic_queue3, pic_queue4, pic_queue5, mode_output_1,  mode_output_2):
        """Khởi tạo class camera"""
        self.pic_queue = pic_queue

        self.pic_queue2 = pic_queue2
        self.pic_queue3 = pic_queue3
        self.pic_queue4 = pic_queue4
        self.pic_queue5 = pic_queue5
        self.group_queues=[self.pic_queue2, self.pic_queue3, self.pic_queue4, self.pic_queue5]

        self.mode_output_1=mode_output_1
        self.mode_output_2=mode_output_2
        self.cameras = []  
        self.cam_special = None  
        self.cam_trigger = None  
        self.cam_group = []  
        self.converter = None
        self.running = True   # Biến kiểm soát vòng lặp thread trigger
        self.trigger_threads = []  

    def begin(self, *args, **kwargs):
        """Mở camera và bắt đầu chụp"""
        try:
            # ✅ Khởi tạo camera
            tlFactory = pylon.TlFactory.GetInstance()
            devices = tlFactory.EnumerateDevices()
            print(f'So cam hien lai là {len(devices)} cams')
            if len(devices) < 5:
                sys.exit() # Không đủ 5 cam thì tắt chương trình luôn
                raise RuntimeError("🚨 Không đủ 5 camera!")

            for i, device in enumerate(devices[:5]):  
                cam = pylon.InstantCamera(tlFactory.CreateDevice(device))
                cam.Open()
                # Turn on limit BrandWidth
                cam.GevSCPSPacketSize.SetValue(9000)  # or 9000 nếu dùng Jumbo Frame
                cam.GevSCPD.SetValue(7895)  # Điều chỉnh theo tải mạng (microseconds)

                cam.StopGrabbing()
                cam.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

                if i == 2:  
                    self.cam_special = cam  # Camera special
                else:
                    if i==3: # Line output trigger 1 - cam group 1
                        self.cam_trigger_1 = cam
                    if i==1: # Line output trigger 2 - cam group 2
                        self.cam_trigger_2 = cam

                    self.cam_group.append(cam)  # 4 camera trong nhóm chạy AI

                self.cameras.append(cam) # Cam riêng lẻ để chạy check bavia

            # ✅ Cấu hình trigger phần cứng
            for i, cam in enumerate(self.cameras):
                cam.LineSelector.SetValue('Line1')  
                cam.LineMode.SetValue('Input')

                if i==2: # cam special
                    cam.ExposureTimeAbs.SetValue(1500)
                elif i==4:
                    cam.ExposureTimeAbs.SetValue(4000)
                else:
                    cam.ExposureTimeAbs.SetValue(5000)

            # ✅ Cấu hình converter cho ảnh
            self.converter = pylon.ImageFormatConverter()
            self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
            self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
            print("✅ 5 Camera đã sẵn sàng!")

            # ✅ Chạy thread cho camera riêng
            thread_special = threading.Thread(target=self.monitor_trigger_special, args=(self.cam_special, self.pic_queue), daemon=True)
            thread_special.start()
            self.trigger_threads.append(thread_special)

            # ✅ Chạy thread riêng cho từng camera nhóm
            for i, cam in enumerate(self.cam_group):
                thread_group = threading.Thread(target=self.monitor_trigger_group, args=(cam, self.group_queues[i]), daemon=True)
                thread_group.start()
                self.trigger_threads.append(thread_group)

            output_basler_1= threading.Thread(target=self.process_mode_output_1, args=(self.mode_output_1,self.cam_trigger_1), daemon=True)
            output_basler_1.start()

            output_basler_2= threading.Thread(target=self.process_mode_output_2, args=(self.mode_output_2,self.cam_trigger_2), daemon=True)
            output_basler_2.start()

        except Exception as e:
            print(f"❌ Lỗi khởi tạo camera: {e}")
            sys.exit()

    def reconnect_camera(self,cam):
        """Thử kết nối lại camera"""
        try:
            cam.Close()
            time.sleep(0.5)
            cam.Open()
            print(f"✅ Camera {cam.GetDeviceInfo().GetSerialNumber()} đã kết nối lại thành công!")
        except Exception as e:
            print(f"⚠ Không thể kết nối lại camera: {e}")

    def monitor_trigger_special(self, cam, queue_target):
        """Luồng riêng cho mỗi camera"""
        previous_status = 0
        while self.running:
            try:
                if cam:
                    status = cam.LineStatus.GetValue()
                    if status == 1 and previous_status == 0:
                        # print(f"🎯 Trigger Camera {cam.GetDeviceInfo().GetSerialNumber()}!")
                        self.trigger_cam(cam, queue_target)
                    previous_status = status
                time.sleep(0.05)

            except pylon.RuntimeException as e:
                # print(f"❌ Lỗi trigger camera {cam.GetDeviceInfo().GetSerialNumber()}: {e}")
                self.reconnect_camera(cam)
                time.sleep(1)

    def monitor_trigger_group(self, cam, queue_target):
        """Luồng riêng cho mỗi camera"""
        previous_status = 0
        while self.running:
            try:
                if cam:
                    status = cam.LineStatus.GetValue()
                    if status == 1 and previous_status == 0:
                        # print(f"🎯 Trigger Camera {cam.GetDeviceInfo().GetSerialNumber()}!")
                        # self.trigger_cam(cam, queue_target)
                        self.trigger_4cam()
                    previous_status = status
                time.sleep(0.008)

            except pylon.RuntimeException as e:
                # print(f"❌ Lỗi trigger camera {cam.GetDeviceInfo().GetSerialNumber()}: {e}")
                self.reconnect_camera(cam)
                time.sleep(1)
                

    def trigger_4cam(self, *args, **kwargs):
        for i, cam in enumerate(self.cam_group):
            time.sleep(0.002)
            self.trigger_cam(cam, self.group_queues[i])
            
    def trigger_cam_special(self, *args, **kwargs):
        self.trigger_cam(self.cam_special, self.pic_queue)
        
    def trigger_cam(self, cam, queue_target):

        """Chụp ảnh từ camera"""
        if cam is None or not cam.IsGrabbing():
            print("⚠ Camera chưa sẵn sàng!")
            return

        try:
            grab_result = cam.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grab_result.GrabSucceeded():
                img = self.converter.Convert(grab_result).GetArray()
                image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                image = cv2.resize(image, (0,0), fx=0.5,fy=0.5)

                # ✅ Kiểm tra trước khi đưa ảnh vào queue
                if not queue_target.full():
                    queue_target.put(image)
                    # print("📸 Ảnh đã được gửi về!")

        except Exception as e:
            # print(f"❌ Lỗi chụp ảnh: {e}")
            sys.exit()

    def process_mode_output_1(self,mode_output,camera): # Chương trình điều chế xuất xung cho Line output1- hệ Cam 1
        time_start_ok=time.time()
        count_start=0
        count_limit=0
        
        while True:
            time.sleep(0.0001)
            try:
                if mode_output.value==1: #ok
                    print('Cam 1 send OK bit')
                    time_start_ok=time.time()
                    count_start=0
                    count_limit=1
                #     print(time_start_ok)
                elif mode_output.value==2: #ng
                    print('Cam 1 send NG bit')
                    count_start=0
                    count_limit=3
                    time_start_ok=time.time()
                mode_output.value=0

                if (time.time()-time_start_ok)<1 and count_start<count_limit:
                    if (time.time()-time_start_ok)>0.05*(1+count_start):# mac dinh do phan cung
                        camera.UserOutputValueAll.SetValue(True)
                        count_start+=1
                        time.sleep(0.02)
                        camera.UserOutputValueAll.SetValue(False)
                    else:
                        pass
                else:
                    pass
            except Exception as e:
                with open('error_log.txt', 'w') as log_file:
                    log_file.write(f'Error in processing_for_picture loop 0: {e}')
                sys.exit()# Không xuất xung chương trình cũng lỗi luôn
                
    def process_mode_output_2(self,mode_output,camera):# Chương trình điều chế xuất xung cho Line output1- hệ 4 Cam
        time_start_ok=time.time()
        count_start=0
        count_limit=0
        
        while True:
            time.sleep(0.0001)
            try:
                if mode_output.value==1: #ok
                    print('Cam 2 send OK bit')
                    time_start_ok=time.time()
                    count_start=0
                    count_limit=1
                #     print(time_start_ok)
                elif mode_output.value==2: #ng
                    print('Cam 2 send NG bit')
                    count_start=0
                    count_limit=3
                    time_start_ok=time.time()
                mode_output.value=0

                if (time.time()-time_start_ok)<1 and count_start<count_limit:
                    if (time.time()-time_start_ok)>0.05*(1+count_start):# mac dinh do phan cung
                        camera.UserOutputValueAll.SetValue(True)
                        count_start+=1
                        time.sleep(0.02)
                        camera.UserOutputValueAll.SetValue(False)
                    else:
                        pass
                else:
                    pass
            except Exception as e:
                with open('error_log.txt', 'w') as log_file:
                    log_file.write(f'Error in processing_for_picture loop 0: {e}')
                sys.exit()# Không xuất xung chương trình cũng lỗi luôn

    def close(self, *args, **kwargs):
        """Dừng camera"""
        self.running = False
        for thread in self.trigger_threads:
            thread.join()

        for cam in self.cameras:
            cam.StopGrabbing()
            cam.Close()
        print("✅ 4 Camera đã được đóng an toàn.")

##---------------------------------------------------------------------##
##---------------------------------------------------------------------##
## Class dùng cho mục đích Calib ảnh

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
    
class FrameCalibrate:

    CAMERA_MATRIX = 'Camera matrix'
    OPPT_CAMERA_MATRIX = 'Optimal camera matrix'
    DISTORT_ROI = 'Distortion ROI'
    DISTORTION = 'Distortion'
    FRAME_SIZE = 'Frame size'

    # Camera calibration matrix
    camera_matrix = []
    optimal_camera_matrix = []
    distort_roi = []
    camera_dist = []
    homo_matrix = []
    frame_size = (0, 0)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    def __init__(self, config_path):
        self.cfg_file_path = str(config_path)
        self.camera_matrix = self.loadMatrix(self.CAMERA_MATRIX)
        self.camera_dist = self.loadMatrix(self.DISTORTION)
        self.frame_size = self.loadMatrix(self.FRAME_SIZE)
        self.optimal_camera_matrix = self.loadMatrix(self.OPPT_CAMERA_MATRIX)
        self.distort_roi = self.loadMatrix(self.DISTORT_ROI)

    def loadMatrix(self, key):
        obj_text = codecs.open(self.cfg_file_path, 'r', encoding='utf-8').read()
        json_load  = json.loads(obj_text)
        value = json_load.get(key)
        if value is not None:
            matrix_restored = np.asarray(json_load[key])
        else:
            matrix_restored = []
        return matrix_restored

    def saveMatrix(self, key, value):
        # print(key)
        # print(value)
        obj_text = codecs.open(self.cfg_file_path, 'r', encoding='utf-8').read()
        json_load  = json.loads(obj_text)
        json_load[key] = np.asarray(value)
        json.dump(json_load, 
                    (codecs.open(self.cfg_file_path, 'w', encoding='utf-8')), 
                    indent=4, 
                    cls=NumpyEncoder)

    def calibrateCameraMatrix(self, input_images_path, grid_size, distance, use_chess_board = True):

        grid_points = np.zeros((grid_size[0] * grid_size[1], 3), np.float32)
        grid_points[:,:2] = np.mgrid[0:grid_size[0],0:grid_size[1]].T.reshape(-1,2)
        grid_points = grid_points * distance

        object_points = []
        image_points = []
        input_images = glob.glob(input_images_path)

        for counter in range(len(input_images)):
            # image = mpimg.imread(input_images[counter], )
            image = cv2.imread(input_images[counter], cv2.IMREAD_GRAYSCALE)

            if (len(image.shape) == 2) :
                gray_image = image
            else :
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            if counter == 0:
                self.frame_size = gray_image.shape[::-1]
                # print(self.frame_size)
                # print(gray_image.shape[::-1])

            if use_chess_board:
                ret, corners = cv2.findChessboardCorners(image, grid_size, None)
            else:
                ret, corners = cv2.findCirclesGrid(image, grid_size, None)

            if ret == True:

                object_points.append(grid_points)
                corners2 = cv2.cornerSubPix(image, corners, (11,11), (-1,-1), self.criteria)
                image_points.append(corners)

                # color_image = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
                image_copy = image.copy()
                color_image = cv2.cvtColor(image_copy, cv2.COLOR_GRAY2BGR)
                cv2.drawChessboardCorners(color_image, grid_size, corners2, ret)
                # save_path = result_images_path.replace('*', str(counter))
                # cv2.imwrite(save_path, image_copy)

            counter += 1
        try:
            ret, self.camera_matrix, self.camera_dist, rvecs, tvecs =  cv2.calibrateCamera(
                                                                        object_points, 
                                                                        image_points, 
                                                                        self.frame_size, 
                                                                        None, None)

            self.optimal_camera_matrix, self.distort_roi = cv2.getOptimalNewCameraMatrix(
                                                    self.camera_matrix,
                                                    self.camera_dist,
                                                    self.frame_size, 1, 
                                                    self.frame_size)

            self.saveMatrix(self.CAMERA_MATRIX, self.camera_matrix)
            self.saveMatrix(self.DISTORTION, self.camera_dist)
            self.saveMatrix(self.FRAME_SIZE, self.frame_size)
            self.saveMatrix(self.OPPT_CAMERA_MATRIX, self.optimal_camera_matrix)
            self.saveMatrix(self.DISTORT_ROI, self.distort_roi)
            return color_image,ret
        except Exception as e:
            print(f"❌ Lỗi calibration: {e}")
            return None,0
        
    def undistortImage(self, image):
        image_undistort = cv2.undistort(image, self.camera_matrix, 
                                        self.camera_dist, None, self.optimal_camera_matrix)

        x, y, w, h = self.distort_roi
        image_undistort = image_undistort[y:y+h, x:x+w]
        return image_undistort
    
##---------------------------------------------------------------------##
##---------------------------------------------------------------------##
## Hàm chạy AI

def run_AI(mode_run_AI,input2, input3, input4, input5, cam2, cam3, cam4, cam5):
    if getattr(sys, 'frozen', False):
        current_file_path = sys._MEIPASS
    else:
        current_file_path = os.path.dirname(os.path.abspath(__file__))
    file_onnx= os.path.join(current_file_path, "model_add_1.onnx")

    # Check GPU support for ONNX Runtime
    print("Available providers:", ort.get_available_providers())
    if 'CUDAExecutionProvider' in ort.get_available_providers():
        ort_sess = ort.InferenceSession(file_onnx, providers=["CUDAExecutionProvider"])
    else:
        ort_sess = ort.InferenceSession(file_onnx)

    w, h = 512, 512

    dummy = np.random.rand(4, h, w,3).astype(np.float32)
    for _ in range(3):  # chạy warm-up 3 lần
        ort_sess.run(None, {"input": dummy})
    
    
    time_start=0
    fps=0

    while mode_run_AI:
        # time.sleep(0.0001)
        # print(f"Queue status: {input2.empty()=}, {input3.empty()=}, {input4.empty()=}, {input5.empty()=}")
        if not input2.empty() and not input3.empty() and not input4.empty() and not input5.empty():
            ## Start time to use caculate FPS
            time_start = time.time()

            image_2= input2.get()
            image_3= input3.get()
            image_4= input4.get()
            image_5= input5.get()
            t_queue_end = time.time()
            # print(f"Time to get all 4 images from queue: {t_queue_end - time_start:.4f} s")

            image_paths=[image_2, image_3, image_4, image_5]
            batch_images = []
            img=None
            batch_images = [cv2.resize(img, (w, h)) for img in image_paths if img is not None]

            batch_images = np.array(batch_images, dtype=np.float32)  # Ensure dtype is float32
            
            # Run inference with ONNX Runtime
            outputs = ort_sess.run(None, {"input": batch_images})[0]

            cam_group=[cam2, cam3, cam4, cam5]

            # Process each output mask
            for i, mask_prediction in enumerate(outputs):
                mask_prediction = (mask_prediction[:,:,0] * 255).astype(np.uint8)  # Take the first channel and convert to 8-bit

                # Resize mask back to original dimensions if needed
                binary_mask = cv2.resize(mask_prediction, (w, h))

                # Create a binary mask with thresholdings
                _, binary_mask = cv2.threshold(binary_mask, 20, 255, cv2.THRESH_BINARY)

                if i < len(cam_group):
                    cam_group[i].put(image_paths[i])
                    cam_group[i].put(binary_mask)

            # Calculate FPS
            fps = 1 / (time.time() - t_queue_end)
            # print(f"FPS: {fps:.2f}")

class UI_of_main_gui(MainWindow):
    # Thay đôi các màn hình đi kèm với mỗi nút 
    def change_window(self, *args, **kwargs):
        # Mảng gồm các nút nhấn đi kèm
        buttons = [
            self.ui.but_tool_cam1, self.ui.but_tool_calib, self.ui.but_tool_4cam,
            self.ui.but_tool_sample, self.ui.but_tool_ng1cam, self.ui.but_tool_ng4cam,
            self.ui.but_tool_output, self.ui.but_tool_view
        ]
        for button in buttons:
            button.clicked.connect(lambda: UI_of_main_gui.toggle_visibility(self))

    def toggle_visibility(self, *args, **kwargs):
        print('cos thay doi')
        self.ui.window_expand.setVisible(not self.ui.window_expand.isVisible())
        self.ui.window_icon.setVisible(not self.ui.window_icon.isVisible())

    # Chuyển đổi giữa các màn hình
    def tranfer_window(self, *args, **kwargs):
         
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
    def update_ram_and_disk_time_and_date(self, *args, **kwargs):

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
    def update_info_time_date(self, *args, **kwargs):

        """Hàm cập nhật thời gian vào QDateTimeEdit"""
        current_time = QDateTime.currentDateTime()
        self.ui.time_and_day.setDateTime(current_time)

    # Cập nhập disk và ram
    def update_info_disk_ram(self, *args, **kwargs):
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
    
    def screen_real_4cam(self, *args, **kwargs):
        self.ui.space_screen1_4cam.setCurrentWidget(self.ui.space_real_1_4cam)
        self.ui.space_screen2_4cam.setCurrentWidget(self.ui.space_real_2_4cam)
        self.ui.space_screen3_4cam.setCurrentWidget(self.ui.space_real_3_4cam)
        self.ui.space_screen4_4cam.setCurrentWidget(self.ui.space_real_4_4cam)
    
    def screen_result_4cam(self, *args, **kwargs):
        self.ui.space_screen1_4cam.setCurrentWidget(self.ui.space_result_1_4cam)
        self.ui.space_screen2_4cam.setCurrentWidget(self.ui.space_result_2_4cam)
        self.ui.space_screen3_4cam.setCurrentWidget(self.ui.space_result_3_4cam)
        self.ui.space_screen4_4cam.setCurrentWidget(self.ui.space_result_4_4cam)     

class Calib(MainWindow):

    # Khởi động xem có bao nhiêu ảnh đang được lưu, tối đa mình chỉ cho lưu 7 ảnh, vì tối thiểu
    # 5 là chạy được rồi
    def start(self, *args, **kwargs):
        image_extensions = {".jpg", ".png", ".jpeg", ".bmp", ".tiff"}

        path_folder=os.path.join(self.current_file_path,'data_calib')

        # Lấy danh sách file trong thư mục (bỏ qua thư mục con)
        files = [f for f in os.listdir(path_folder) 
                if os.path.isfile(os.path.join(path_folder, f)) and 
                os.path.splitext(f)[1].lower() in image_extensions
            ]
        
        self.file_count_calib = len(files)

        self.current_label.setText(f"Hiện có: {self.file_count_calib}")
        self.current_label.setStyleSheet(f"background-color: white;")

    # Lấy ảnh mới nhất để show trên label
    def check_file_in_folder(self, *args, **kwargs):
        image_extensions = {".jpg", ".png", ".jpeg", ".bmp", ".tiff"}
        

        path_folder=os.path.join(self.current_file_path,'data_calib')

        # Lấy danh sách file trong thư mục (bỏ qua thư mục con)
        files = [f for f in os.listdir(path_folder) 
                if os.path.isfile(os.path.join(path_folder, f)) and 
                os.path.splitext(f)[1].lower() in image_extensions
            ]

        # Sắp xếp file theo thứ tự tự nhiên
        sorted_files = natsorted(files)

        # Kiểm tra số lượng file
        self.file_count_calib = len(sorted_files)

        # Lấy file mới nhất (nếu có)
        if sorted_files:
            latest_image = max(sorted_files, key=lambda f: os.path.getmtime(os.path.join(path_folder, f)))
            # print(f"File ảnh mới nhất theo thời gian: {latest_image}")
            latest_image_path = os.path.join(path_folder, latest_image)
            if os.path.exists(latest_image_path):
                image=cv2.imread(latest_image_path)
                UI_of_main_gui.show_image_3chanel(self,image,self.ui.show_pic_calib_calib)
        else:
            self.ui.show_pic_calib_calib.clear()

        
        self.current_label.setText(f"Hiện có: {self.file_count_calib}")
        self.current_label.setStyleSheet(f"background-color: white;")

    # Xóa số ảnh đang có dùng cho Calib
    def clear_file_image(self, *args, **kwargs):
        # Định dạng file ảnh cần xóa
        image_extensions = {".jpg", ".png", ".jpeg", ".bmp", ".tiff"}
        

        # Đường dẫn thư mục
        path_folder = os.path.join(self.current_file_path, 'data_calib')

        # Duyệt qua tất cả các file trong thư mục
        for file in os.listdir(path_folder):
            file_path = os.path.join(path_folder, file)
            
            # Kiểm tra nếu là file ảnh
            if os.path.isfile(file_path) and os.path.splitext(file)[1].lower() in image_extensions:
                os.remove(file_path)  # Xóa file

        Calib.check_file_in_folder(self)

class Cam_1(MainWindow):
    def __init__(self):
        super().__init__()
        
    # Bắt đầu đọc các file đã lưu và gán định giá trị ương tứng
    def start(self, *args, **kwargs):
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
    def undo_data(self, *args, **kwargs):
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
    def slider_change_value_cam1(self, *args, **kwargs):

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
    def define_value_cam1(self, *args, **kwargs):
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
    def define_value_4cam(self, *args, **kwargs):
        self.value_4cam[0]=int(self.ui.slider_limit_area_4cam.value())

        Cam_1.update_slider_4cam(self,self.value_4cam)
        Cam_1.update_text_4cam(self,self.value_4cam)
        Cam_1.update_value_file_4cam(self)

        self.slider_timer2.start(10)# Bắt đầu timer chỉ cập nhập sau 0.01s

    # Check xem có phải số nguyên INT không với riêng phần Sản lượng
    def check_value_line_edit_production(self, *args, **kwargs):
        value= self.ui.lineEdit.text()
        if Cam_1.Check_convert_str_to_int(self,value)==True:
            return int(value)
        else:
            return 0

    # Check xem có là giá trị float không nếu không cho về bằng 0.0 đặc biệt với QlineEdit
    def check_value_line_edit(self, *args, **kwargs):
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
    def update_value_file_cam1(self, *args, **kwargs):
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
    def update_value_file_4cam(self, *args, **kwargs):
        path_folder=os.path.join(self.current_file_path,'data_txt','value_cam2.txt')
        data=open(path_folder, "w")
        data_all_4cam = [ str(self.value_4cam[0])+"\n"
                    ]
        
        data.writelines(data_all_4cam)
        data.close()
    
    # Chuyển đổi giữa các trang với cam 1
    def switch_page(self, *args, **kwargs):

        """Chuyển đổi giữa hai trang"""
        current_index = self.ui.stackedWidget_2.currentIndex()
        # new_index = 1 if current_index == 0 else 0  # Nếu 0 → 1, nếu 1 → 0
        new_index = (current_index + 1) % 3  # Xoay vòng qua 0 → 1 → 2 → 0
        self.ui.stackedWidget_2.setCurrentIndex(new_index)
    
    def switch_page_right(self, *args, **kwargs):
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
    
    def switch_page_left(self, *args, **kwargs):
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

class Sample():
    # Khởi chạy, đọc và gán giá trị lúc bạn đầu
    def __init__(self, parent: "MainWindow"):
        self.parent = parent
        # Lấy đường dẫn tuyệt đối của file đang chạy 
        self.current_file_path = os.path.dirname(os.path.abspath(__file__))
        self.sample_path = os.path.join(self.current_file_path, "picture", "sample_cam1.png")

        self.masked_image=None

        # Đọc ảnh gốc
        self.image_original_sample = cv2.imread(self.sample_path)
        self.image_original_sample = cv2.cvtColor(self.image_original_sample, cv2.COLOR_BGR2RGB)

        self.image = self.image_original_sample.copy()  # Sao chép ảnh để vẽ mà không làm mất ảnh gốc

        self.center_sample = None
        self.radius_sample = 0
        self.dragging_sample = False  # Trạng thái kéo hình tròn

        self.temporary_sample= []
        self.point_circle_back_path = os.path.join(self.current_file_path, "data_txt", "point_circle_sample.txt")
        self.data_sample= self.read_value_file_back(self.point_circle_back_path)

        # Gán ảnh lên QLabel
        self.display_image(self.image, self.parent.ui.show_pic_real_sample)
        # UI_of_main_gui.show_image_3chanel(self,self.image, self.parent.ui.show_pic_real_sample)

        # Sự kiện chuột
        self.parent.ui.show_pic_real_sample.mousePressEvent = self.mouse_press_event
        self.parent.ui.show_pic_real_sample.mouseMoveEvent = self.mouse_move_event
        self.parent.ui.show_pic_real_sample.mouseReleaseEvent = self.mouse_release_event

        self.parent.ui.but_sample_sample.clicked.connect(self.function_button_take_sample)
        self.parent.ui.but_clear_sample.clicked.connect(self.function_button_clear_sample)
     
    def reset(self, *args, **kwargs):
        """Cập nhật ảnh mới và vẽ lại nếu có hình tròn"""
        self.image_original_sample = cv2.imread(self.sample_path)
        self.image_original_sample = cv2.cvtColor(self.image_original_sample, cv2.COLOR_BGR2RGB)
        self.image = self.image_original_sample.copy()

        if self.center_sample and self.radius_sample > 0:
            cv2.circle(self.image, self.center_sample, self.radius_sample, (0, 150, 255), 2)

            mask = np.zeros_like(self.image_original_sample, dtype=np.uint8)
            cv2.circle(mask, self.center_sample, self.radius_sample, (255, 255, 255), -1)
            show = cv2.bitwise_and(self.image_original_sample, mask)

            self.display_image(show, self.parent.ui.show_pic_sample_sample)

        self.display_image(self.image, self.parent.ui.show_pic_real_sample)
        print("Ảnh đã được cập nhật và hiển thị")
       

    def read_value_file_back(self, file_name):
        points=[]
        with open(file_name, "r") as file:
            lines = file.readlines()

            if not lines:
                return []
            # Đọc các giá trị tâm và R để xác định hình tròn để vẽ
            for line in lines:
                if line.strip():
                    x1, x2, x3 = map(int, line.strip().split())
                    points.append((x1, x2, x3))

                    self.center_sample= (x1,x2)
                    self.radius_sample= x3
                    self.update_display((0,150,255)) # chỉ chọn màu thôi
        return points
    
    def mouse_press_event(self, event):

        if not self.data_sample:
            """Xử lý sự kiện nhấn chuột."""

            if self.parent.ui.show_pic_real_sample.pixmap() is None :
                return
            
            x, y = self.convert_label_to_image_coords(event)

            # Kiểm tra nếu nhấn gần tâm hình tròn → Bật chế độ kéo
            if self.center_sample and self.radius_sample > 0:
                print(self.center_sample)
                distance = math.sqrt((x - self.center_sample[0]) ** 2 + (y - self.center_sample[1]) ** 2)
                if distance < self.radius_sample * 0.3:  # Nếu nhấn trong 30% bán kính hình tròn
                    self.dragging_sample = True
                    return

            # Nếu không nhấn vào hình tròn, vẽ hình mới
            self.center_sample = (x, y)
            self.radius_sample = 0
            self.dragging_sample = False
            self.image = self.image_original_sample.copy()
            self.display_image(self.image, self.parent.ui.show_pic_real_sample)

    def convert_label_to_image_coords(self, event):
        """Chuyển đổi tọa độ từ QLabel về tọa độ thực trong ảnh gốc."""
        label_width = self.parent.ui.show_pic_real_sample.width()
        label_height = self.parent.ui.show_pic_real_sample.height()
        img_height, img_width, _ = self.image_original_sample.shape

        scale_x = img_width / label_width
        scale_y = img_height / label_height

        x = int(event.pos().x() * scale_x)
        y = int(event.pos().y() * scale_y)
        return x, y
    
    def mouse_move_event(self, event):
        if not self.data_sample:
            self.temporary_sample=[]
            """Xử lý sự kiện kéo chuột."""
            if self.parent.ui.show_pic_real_sample.pixmap() is None:
                return

            x, y = self.convert_label_to_image_coords(event)

            if self.dragging_sample:
                # Di chuyển hình tròn thay vì vẽ lại
                self.center_sample = (x, y)
            elif self.center_sample:
                # Vẽ hình tròn mới nếu không kéo
                self.radius_sample = int(math.sqrt((x - self.center_sample[0]) ** 2 + (y - self.center_sample[1]) ** 2))

            self.temporary_sample.append((self.center_sample[0], self.center_sample[1], self.radius_sample))

            # Cập nhật ảnh
            self.update_display()

    def update_display(self, color=(255, 0, 0)):
        """Cập nhật QLabel với hình tròn hiện tại."""
        self.image = self.image_original_sample.copy()
        if self.center_sample and self.radius_sample > 0:
            cv2.circle(self.image, self.center_sample, self.radius_sample, color, 2)

            # Tạo mặt nạ và hiển thị vùng trong hình tròn trên QLabel `out`
            mask = np.zeros_like(self.image_original_sample, dtype=np.uint8)
            cv2.circle(mask, self.center_sample, self.radius_sample, (255, 255, 255), -1)
            show = cv2.bitwise_and(self.image_original_sample, mask)

            self.display_image(show, self.parent.ui.show_pic_sample_sample)
            # Hình ảnh vùng cần lấy
            # Mở rộng kích thước mặt nạ hình vuông
            expand_size = self.radius_sample + 2  # Tăng kích thước 10px so với hình tròn
            x1 = max(0, self.center_sample[0] - expand_size)
            y1 = max(0, self.center_sample[1] - expand_size)
            x2 = min(self.image_original_sample.shape[1], self.center_sample[0] + expand_size)
            y2 = min(self.image_original_sample.shape[0], self.center_sample[1] + expand_size)
            self.masked_image = show[y1:y2, x1:x2].copy()

            # cv2.imwrite('ok1.png',masked_image)
        self.display_image(self.image, self.parent.ui.show_pic_real_sample)

    def display_image(self, image, label):
        """Hiển thị ảnh OpenCV trên QLabel."""
        h, w, ch = image.shape
        bytes_per_line = ch * w
        q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(q_image))
        label.setScaledContents(True)  # Đảm bảo ảnh vừa với QLabel

    def mouse_release_event(self, event):
        """Xử lý sự kiện nhả chuột."""
        self.dragging_sample = False  # Dừng kéo hình tròn

    def function_button_take_sample(self):
        # if not self.temporary:
        self.data_sample= self.temporary_sample
        ## Saving data into local
        data_backup_write=open(self.point_circle_back_path,"w")
        data_all_write = ""
        for point in self.data_sample:
            data_all_write += f"{point[0]} {point[1]} {point[2]}"
        data_backup_write.write(data_all_write)
        data_backup_write.close()
        
        self.update_display((0,150,255))
        link = os.path.join(self.current_file_path, "picture", "saved_sample.png")
        cv2.imwrite(link,self.masked_image)
    
    def function_button_clear_sample(self):
        self.data_sample= []
        data_backup_write=open(self.point_circle_back_path,"w")
        data_all_write = ""
        for point in self.data_sample:
            data_all_write += f"{point[0]} {point[1]} {point[2]}"
        data_backup_write.write(data_all_write)
        data_backup_write.close()

        # self.center= (x1,x2)
        self.radius_sample= 0

        self.update_display()
        self.parent.ui.show_pic_sample_sample.clear()

class ListWidget():
    def __init__(self, parent: "MainWindow"):

        self.parent = parent

        self.list_NG_cam1()
        self.parent.ui.list_ng1cam.clicked.connect(self.show_img_NG_cam1)
        self.parent.ui.but_up_ng1cam.clicked.connect(self.up_currentRow_cam1)
        self.parent.ui.but_down_ng1cam.clicked.connect(self.down_currentRow_cam1)

        self.list_NG_4cam()
        self.parent.ui.list_ng4cam.clicked.connect(self.show_img_NG_4cam)
        self.parent.ui.but_up_ng4cam.clicked.connect(self.up_currentRow_4cam)
        self.parent.ui.but_down_ng4cam.clicked.connect(self.down_currentRow_4cam)


    def list_NG_cam1(self, *args, **kwargs):

        filenames = self.parent.get_recent_filenames(self.parent.database[0])

        # Xóa danh sách cũ trước khi thêm mới
        self.parent.ui.list_ng1cam.clear() 
        if filenames:
            self.parent.ui.list_ng1cam.addItems(filenames)  # Thêm dữ liệu vào QListWidget
            print(f"✅ Đã tải NG cam 1 co {len(filenames)} file vào ListWidget")
        else:
            print("⚠️ Không có file nào trong database!")

    def list_NG_4cam(self, *args, **kwargs):

        filenames = self.parent.get_recent_filenames(self.parent.database[1])

        # Xóa danh sách cũ trước khi thêm mới
        self.parent.ui.list_ng4cam.clear() 
        if filenames:
            self.parent.ui.list_ng4cam.addItems(filenames)  # Thêm dữ liệu vào QListWidget
            print(f"✅ Đã tải NG 4 cam co {len(filenames)} file vào ListWidget")
        else:
            print("⚠️ Không có file nào trong database!")

    def show_img_NG_cam1(self, *args, **kwargs):
        item_img_ng = self.parent.ui.list_ng1cam.currentItem()
        if item_img_ng is not None:
            item_img_ng = item_img_ng.text()
            # print(self.parent.real_path_ng_cam1)
            # Lấy link 2 cái ảnh
            link_real_image= os.path.join(self.parent.real_path_ng_cam1, item_img_ng)
            link_virtual_image= os.path.join(self.parent.virtual_path_ng_cam1, item_img_ng)

            real_image=cv2.imread(link_real_image)
            virtual_image=cv2.imread(link_virtual_image)

            UI_of_main_gui.show_image_3chanel(self.parent,real_image, self.parent.ui.show_pic_real_ng1cam)
            UI_of_main_gui.show_image_3chanel(self.parent,virtual_image, self.parent.ui.show_pic_result_ng1cam)

    def show_img_NG_4cam(self, *args, **kwargs):
        item_img_ng = self.parent.ui.list_ng4cam.currentItem()
        if item_img_ng is not None:
            item_img_ng = item_img_ng.text()

            # Lấy link 2 cái ảnh
            pic_real=[self.parent.ui.show_pic_real_1_ng4cam, self.parent.ui.show_pic_real_2_ng4cam,
                      self.parent.ui.show_pic_real_3_ng4cam, self.parent.ui.show_pic_real_4_ng4cam]
            
            pic_result=[self.parent.ui.show_pic_result_1_ng4cam, self.parent.ui.show_pic_result_2_ng4cam,
                        self.parent.ui.show_pic_result_3_ng4cam, self.parent.ui.show_pic_result_4_ng4cam]
            
            for i in range(2,6):
                link_real_path_ng4cam= os.path.join(self.parent.real_path_ng_4cam, f"cam{i}", item_img_ng)
                link_virtual_ng4cam= os.path.join(self.parent.virtual_path_ng_4cam, f"cam{i}", item_img_ng)

                real_image=cv2.imread(link_real_path_ng4cam)
                virtual_image=cv2.imread(link_virtual_ng4cam)

                UI_of_main_gui.show_image_3chanel(self.parent,real_image, pic_real[i-2] )
                UI_of_main_gui.show_image_3chanel(self.parent,virtual_image, pic_result[i-2])

    def up_currentRow_cam1(self, *args, **kwargs):
        # count= self.ui.listWidget_NG.count()
        current_row= self.parent.ui.list_ng1cam.currentRow()
        if current_row>=1:
            current_row-=1
            self.parent.ui.list_ng1cam.setCurrentRow(current_row)
            self.show_img_NG_cam1()

    def up_currentRow_4cam(self, *args, **kwargs):
        current_row= self.parent.ui.list_ng4cam.currentRow()
        if current_row>=1:
            current_row-=1
            self.parent.ui.list_ng4cam.setCurrentRow(current_row)
            self.show_img_NG_4cam()

    def down_currentRow_cam1(self, *args, **kwargs):
        #### Xem so luong file trong path
        count_limit= self.parent.ui.list_ng1cam.count()

        current_row= self.parent.ui.list_ng1cam.currentRow()
        # print(current_row)
        if current_row< min(199, count_limit - 1):
            current_row+=1
            self.parent.ui.list_ng1cam.setCurrentRow(current_row)
            self.show_img_NG_cam1()

    def down_currentRow_4cam(self, *args, **kwargs):
        #### Xem so luong file trong path
        count_limit= self.parent.ui.list_ng4cam.count()

        current_row= self.parent.ui.list_ng4cam.currentRow()
        # print(current_row)
        if current_row< min(199, count_limit - 1):
            current_row+=1
            self.parent.ui.list_ng4cam.setCurrentRow(current_row)
            self.show_img_NG_4cam()

def run_main():
    multiprocessing.freeze_support()
    ### Convert 
    # auto_tranfer_file.convert_ui_qrc_to_py()
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

# if __name__ == "__main__":
#     multiprocessing.freeze_support()
#     ## Convert 
#     # auto_tranfer_file.convert_ui_qrc_to_py()
#     app = QApplication(sys.argv)
#     main_win = MainWindow()
#     main_win.show()
#     sys.exit(app.exec())

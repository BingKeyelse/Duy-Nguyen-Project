import sys
import cv2
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
from multiprocessing import Queue
import queue
from pypylon import pylon
import threading


from test import Ui_MainWindow  # Import file giao diện PyQt5

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ✅ Khởi tạo Queue để truyền ảnh từ camera đến GUI
        self.pic_queue = queue.Queue()

        # ✅ Khởi tạo camera Basler
        self.camera = camera_Basler_multi(self.pic_queue)
        self.camera.begin()

        # ✅ Kết nối nút với trigger camera
        self.ui.button.clicked.connect(self.trigger_cam)

        # ✅ Chạy thread hiển thị ảnh
        thread1 = threading.Thread(target=self.display, daemon=True)
        thread1.start()

    def trigger_cam(self):
        """Gọi trigger để chụp ảnh"""
        self.camera.trigger_cam()
    
    def display(self):
        while True:
            time.sleep(0.01)  # Tránh chiếm quá nhiều CPU
            if not self.pic_queue.empty():
                image = self.pic_queue.get()

                initial_size = self.ui.label.size()
                resized_img2 = cv2.resize(image, (initial_size.width(), initial_size.height()), interpolation=cv2.INTER_LINEAR)
                img_height, img_width, img_channel = resized_img2.shape
                q_image = QImage(resized_img2.data, img_width, img_height, img_width * img_channel, QImage.Format.Format_RGB888)
                pixmap = QPixmap.fromImage(q_image)
                self.ui.label.setPixmap(pixmap)
    
    def closeEvent(self, event):
        print("Ngắt kết nối camera thoát chương trình")
        self.camera.close()
        event.accept()

class camera_Basler_multi:
    def __init__(self, pic_queue):
        """Khởi tạo class camera"""
        self.pic_queue = pic_queue
        self.cam = None
        self.converter = None
        self.running = True  # Biến kiểm soát vòng lặp thread trigger

    def begin(self):
        """Mở camera và bắt đầu chụp"""
        try:
            # ✅ Khởi tạo camera
            tlFactory = pylon.TlFactory.GetInstance()
            devices = tlFactory.EnumerateDevices()

            if len(devices) == 0:
                raise RuntimeError("🚨 Không tìm thấy camera!")

            self.cam = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            self.cam.Open()
            self.cam.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

            # ✅ Cấu hình trigger phần cứng
            self.cam.LineSelector.SetValue('Line1')  
            self.cam.LineMode.SetValue('Input')

            # ✅ Cấu hình converter cho ảnh
            self.converter = pylon.ImageFormatConverter()
            self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
            self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

            print("✅ Camera đã sẵn sàng!")

            # ✅ Bắt đầu theo dõi tín hiệu trigger phần cứng
            self.trigger_thread = self.monitor_trigger()
            self.trigger_thread.start()

        except Exception as e:
            print(f"❌ Lỗi khởi tạo camera: {e}")
    
    def monitor_trigger(self):
        def run():
            """Luồng chạy liên tục kiểm tra tín hiệu từ Line1"""
            previous_status = 0  # Trạng thái trước đó của Line1
            while self.running:
                try:
                    line_status = self.cam.LineStatus.GetValue()
                    if line_status == 1 and previous_status == 0:  # Chỉ chụp khi có sự thay đổi từ 0 → 1
                        print("🎯 Tín hiệu kích hoạt! Chụp ảnh...")
                        self.trigger_cam()

                    previous_status = line_status  # Cập nhật trạng thái
                    time.sleep(0.005)  # Tránh tiêu tốn CPU quá nhiều
                except Exception as e:
                    print(f"❌ Lỗi khi theo dõi trigger: {e}")
        return  threading.Thread(target=run, daemon=True)

    def trigger_cam(self):
        """Chụp ảnh từ camera"""
        if self.cam is None or not self.cam.IsGrabbing():
            print("⚠ Camera chưa sẵn sàng!")
            return

        try:
            grab_result = self.cam.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grab_result.GrabSucceeded():
                img = self.converter.Convert(grab_result).GetArray()
                image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # ✅ Kiểm tra trước khi đưa ảnh vào queue
                if not self.pic_queue.full():
                    self.pic_queue.put(image)
                    print("📸 Ảnh đã được gửi về GUI!")

        except Exception as e:
            print(f"❌ Lỗi chụp ảnh: {e}")

    def close(self):
        # self.running=False
        self.running=False
        if self.trigger_thread is not None:
            self.trigger_thread.join()
        """Dừng camera"""
        self.cam.StopGrabbing()
        self.cam.Close()
        
        print("✅ Camera đã được đóng an toàn.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

import threading
import time
import cv2
from pypylon import pylon
from queue import Queue

class CameraBaslerMulti:
    def __init__(self, pic_queue, mode):
        """Khởi tạo class camera"""
        self.pic_queue = pic_queue
        self.mode = mode
        self.cameras = []  # Danh sách camera
        self.threads = []  # Danh sách luồng xử lý camera
        self.converter = None
        self.running = True  

    def begin(self):
        """Mở camera và khởi động luồng chụp ảnh"""
        try:
            # ✅ Khởi tạo danh sách camera
            tlFactory = pylon.TlFactory.GetInstance()
            devices = tlFactory.EnumerateDevices()

            if len(devices) < 4:
                raise RuntimeError("🚨 Không đủ 4 camera!")

            # ✅ Mở tất cả 4 camera
            for device in devices[:4]:  
                cam = pylon.InstantCamera(tlFactory.CreateDevice(device))
                cam.Open()
                cam.StopGrabbing()
                cam.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                self.cameras.append(cam)

            # ✅ Cấu hình trigger phần cứng cho từng camera
            for cam in self.cameras:
                cam.LineSelector.SetValue('Line1')  
                cam.LineMode.SetValue('Input')

            # ✅ Cấu hình converter ảnh
            self.converter = pylon.ImageFormatConverter()
            self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
            self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

            print("✅ 4 Camera đã sẵn sàng!")

            # ✅ Tạo luồng xử lý ảnh cho từng camera
            for cam in self.cameras:
                thread = threading.Thread(target=self.capture_loop, args=(cam,), daemon=True)
                thread.start()
                self.threads.append(thread)

        except Exception as e:
            print(f"❌ Lỗi khởi tạo camera: {e}")

    def capture_loop(self, cam):
        """Luồng chạy liên tục để kiểm tra trigger và chụp ảnh"""
        previous_status = 0
        while self.running:
            try:
                status = cam.LineStatus.GetValue()
                if status == 1 and previous_status == 0:
                    self.trigger_cam(cam)
                previous_status = status
                time.sleep(0.008)  # Giảm tải CPU

            except pylon.RuntimeException as e:
                print(f"❌ Lỗi trigger: {e}")
                self.reconnect_camera(cam)
                time.sleep(1)

            except Exception as e:
                print(f"❌ Lỗi khác: {e}")
                time.sleep(1)

    def reconnect_camera(self, cam):
        """Thử kết nối lại camera"""
        try:
            cam.Close()
            time.sleep(0.5)
            cam.Open()
            print(f"✅ Camera {cam.GetDeviceInfo().GetSerialNumber()} đã kết nối lại thành công!")
        except Exception as e:
            print(f"⚠ Không thể kết nối lại camera: {e}")

    def trigger_cam(self, cam):
        """Chụp ảnh từ một camera cụ thể"""
        if cam is None or not cam.IsGrabbing():
            print("⚠ Camera chưa sẵn sàng!")
            return

        try:
            grab_result = cam.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grab_result.GrabSucceeded():
                img = self.converter.Convert(grab_result).GetArray()
                image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # ✅ Đưa ảnh vào queue
                if not self.pic_queue.full():
                    self.pic_queue.put(image)
                    print(f"📸 Ảnh từ camera {cam.GetDeviceInfo().GetSerialNumber()} đã gửi về GUI!")

        except Exception as e:
            print(f"❌ Lỗi chụp ảnh: {e}")

    def close(self):
        """Dừng camera"""
        self.running = False
        for thread in self.threads:
            thread.join()

        for cam in self.cameras:
            cam.StopGrabbing()
            cam.Close()

        print("✅ 4 Camera đã được đóng an toàn.")


# ===== TEST CODE =====
if __name__ == "__main__":
    pic_queue = Queue(maxsize=10)
    camera_system = CameraBaslerMulti(pic_queue, mode="test")
    camera_system.begin()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 Đang đóng camera...")
        camera_system.close()

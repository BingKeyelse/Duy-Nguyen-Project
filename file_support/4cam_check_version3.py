import threading
import time
import cv2
from pypylon import pylon
import queue

class CameraBaslerMulti:
    def __init__(self):
        """Khởi tạo class camera"""
        self.special_queue = queue.Queue(maxsize=10)  # Queue riêng cho camera đặc biệt
        self.group_queues = [queue.Queue(maxsize=10) for _ in range(3)]  # 3 queue riêng cho từng cam nhóm
        self.cameras = []  
        self.cam_special = None  
        self.cam_group = []  
        self.converter = None
        self.running = True  
        self.trigger_threads = []  

    def begin(self):
        """Mở camera và bắt đầu chụp"""
        try:
            tlFactory = pylon.TlFactory.GetInstance()
            devices = tlFactory.EnumerateDevices()
            if len(devices) < 4:
                raise RuntimeError("🚨 Không đủ 4 camera!")

            for i, device in enumerate(devices[:4]):  
                cam = pylon.InstantCamera(tlFactory.CreateDevice(device))
                cam.Open()
                cam.StopGrabbing()
                cam.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

                if i == 0:  
                    self.cam_special = cam  # Camera riêng
                else:
                    self.cam_group.append(cam)  # 3 camera nhóm

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

            # ✅ Chạy thread cho camera riêng
            thread_special = threading.Thread(target=self.monitor_trigger, args=(self.cam_special, self.special_queue), daemon=True)
            thread_special.start()
            self.trigger_threads.append(thread_special)

            # ✅ Chạy thread riêng cho từng camera nhóm
            for i, cam in enumerate(self.cam_group):
                thread_group = threading.Thread(target=self.monitor_trigger, args=(cam, self.group_queues[i]), daemon=True)
                thread_group.start()
                self.trigger_threads.append(thread_group)

        except Exception as e:
            print(f"❌ Lỗi khởi tạo camera: {e}")

    def monitor_trigger(self, cam, queue_target):
        """Luồng riêng cho mỗi camera"""
        previous_status = 0

        while self.running:
            try:
                if cam:
                    status = cam.LineStatus.GetValue()
                    if status == 1 and previous_status == 0:
                        print(f"🎯 Trigger Camera {cam.GetDeviceInfo().GetSerialNumber()}!")
                        self.trigger_cam(cam, queue_target)
                    previous_status = status
                time.sleep(0.008)

            except pylon.RuntimeException as e:
                print(f"❌ Lỗi trigger camera {cam.GetDeviceInfo().GetSerialNumber()}: {e}")
                self.reconnect_camera(cam)
                time.sleep(1)

    def trigger_cam(self, cam, queue_target):
        """Chụp ảnh từ một camera và đưa vào queue tương ứng"""
        if cam is None or not cam.IsGrabbing():
            print("⚠ Camera chưa sẵn sàng!")
            return

        try:
            grab_result = cam.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grab_result.GrabSucceeded():
                img = self.converter.Convert(grab_result).GetArray()
                image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # ✅ Đưa ảnh vào queue phù hợp
                if not queue_target.full():
                    queue_target.put(image)
                    print(f"📸 Ảnh từ camera {cam.GetDeviceInfo().GetSerialNumber()} đã gửi vào queue!")

        except Exception as e:
            print(f"❌ Lỗi chụp ảnh: {e}")

    def reconnect_camera(self, cam):
        """Thử kết nối lại camera"""
        try:
            cam.Close()
            time.sleep(0.5)
            cam.Open()
            print(f"✅ Camera {cam.GetDeviceInfo().GetSerialNumber()} đã kết nối lại thành công!")
        except Exception as e:
            print(f"⚠ Không thể kết nối lại camera: {e}")

    def close(self):
        """Dừng camera"""
        self.running = False
        for thread in self.trigger_threads:
            thread.join()

        for cam in self.cameras:
            cam.StopGrabbing()
            cam.Close()

        print("✅ 4 Camera đã được đóng an toàn.")

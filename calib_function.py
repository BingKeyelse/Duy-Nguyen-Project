
from import_all import*

class Calib(MainWindow):

    # Khởi động xem có bao nhiêu ảnh đang được lưu, tối đa mình chỉ cho lưu 7 ảnh, vì tối thiểu
    # 5 là chạy được rồi
    def start(self):
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
    def check_file_in_folder(self):
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
    def clear_file_image(self):
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
        
import cv2
import os

# Thư mục chứa ảnh
input_folder = "data_calib"  # Đổi thành đường dẫn thư mục của bạn

# Lặp qua tất cả các file trong thư mục
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):  # Kiểm tra file có phải .png không
        img_path = os.path.join(input_folder, filename)  # Đường dẫn đầy đủ
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)  # Đọc ảnh
        
        if img is not None:
            # Tạo tên file mới với đuôi .bmp
            new_filename = os.path.splitext(filename)[0] + ".bmp"
            new_path = os.path.join(input_folder, new_filename)
            
            # Lưu ảnh dưới dạng .bmp
            cv2.imwrite(new_path, img)
            print(f"Đã chuyển {filename} → {new_filename}")
        else:
            print(f"Lỗi đọc ảnh: {filename}")

print("✅ Hoàn tất chuyển đổi!")

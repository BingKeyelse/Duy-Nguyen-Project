import os
import cv2

# ✅ Đường dẫn thư mục gốc và thư mục lưu ảnh sau khi resize
source_folder = 'data_cam_group/sum_group'
destination_folder = "data_cam_group/NG_group"

# ✅ Tạo thư mục đích nếu chưa tồn tại
os.makedirs(destination_folder, exist_ok=True)

# ✅ Lặp qua tất cả file trong thư mục gốc
for file_name in os.listdir(source_folder):
    src_path = os.path.join(source_folder, file_name)

    # Kiểm tra là file ảnh (dựa vào đuôi)
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff')):
        try:
            # Đọc ảnh
            img = cv2.imread(src_path)
            if img is None:
                print(f"⚠️ Không đọc được ảnh: {file_name}")
                continue

            # Resize ảnh (tỉ lệ 0.5x0.5)
            resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

            # Đường dẫn ảnh sau khi resize
            dst_path = os.path.join(destination_folder, file_name)

            # Lưu ảnh
            cv2.imwrite(dst_path, resized_img)
            print(f"✅ Đã lưu: {dst_path}")
        except Exception as e:
            print(f"❌ Lỗi khi xử lý ảnh {file_name}: {e}")

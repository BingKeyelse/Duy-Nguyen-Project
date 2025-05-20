import os
import random
import shutil

# ✅ Đường dẫn thư mục gốc và thư mục đích
source_folder = r'data_cam_group/NG_add'
destination_folder = r'data_cam_group/ng_add_100'

# ✅ Tạo thư mục đích nếu chưa tồn tại
os.makedirs(destination_folder, exist_ok=True)

# ✅ Lấy danh sách tất cả các file trong thư mục gốc
all_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# ✅ Lấy ngẫu nhiên 50 file (hoặc ít hơn nếu không đủ)
num_files_to_copy = min(100, len(all_files))
random_files = random.sample(all_files, num_files_to_copy)

# ✅ Thực hiện sao chép
for file_name in random_files:
    src_path = os.path.join(source_folder, file_name)
    dst_path = os.path.join(destination_folder, file_name)
    shutil.copy2(src_path, dst_path)  # copy2 giữ nguyên metadata
    print(f"✅ Đã sao chép: {file_name}")

print(f"\n🎉 Đã sao chép {len(random_files)} file từ '{source_folder}' đến '{destination_folder}'")

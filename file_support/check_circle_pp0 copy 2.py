import cv2
import numpy as np
import time

while True:
    time_start = time.time()

    # Đọc ảnh đầu vào
    image = cv2.imread(r"picture\test_circle.png", cv2.IMREAD_GRAYSCALE)

    # Nhị phân hóa ảnh để lấy vùng hình tròn
    _, binary = cv2.threshold(image, 20, 255, cv2.THRESH_BINARY)

    # Tìm contour lớn nhất (hình tròn)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        print("Không tìm thấy hình tròn trong ảnh.")
        exit()

    largest_contour = max(contours, key=cv2.contourArea)

    # Xác định tâm bằng bounding box của contour
    x, y, w, h = cv2.boundingRect(largest_contour)
    cx, cy = int(x + w / 2), int(y + h / 2)  # Tâm của bounding box

    # Tạo mask từ contour
    mask = np.zeros_like(image)
    cv2.drawContours(mask, [largest_contour], -1, 255, thickness=1)

    h, w = mask.shape


    # Tạo ảnh màu để vẽ kết quả
    output = cv2.cvtColor(mask.copy(), cv2.COLOR_GRAY2BGR)

    # 🔹 **BƯỚC 1: Tạo bảng góc trước**
    angles_ref = np.linspace(0, 360, 360, endpoint=False)  # 360 giá trị từ 0° đến 359°

    # 🔹 **BƯỚC 2: Tính toán nhanh góc & khoảng cách**
    contour_points = largest_contour[:, 0, :]  # Lấy danh sách các điểm biên

    # Tính khoảng cách từ tâm đến từng điểm biên
    dx = contour_points[:, 0] - cx
    dy = contour_points[:, 1] - cy
    distances = np.sqrt(dx**2 + dy**2)

    # Tính góc của từng điểm so với tâm
    angles = np.arctan2(dy, dx) * 180 / np.pi  # Chuyển đổi sang độ
    angles = np.mod(angles, 360)  # Đảm bảo góc trong khoảng 0-360

    # 🔹 **BƯỚC 3: Ánh xạ khoảng cách vào mảng `r_list`**
    r_list = np.full(360, np.nan)

    # Tìm góc gần nhất trong `angles_ref` bằng broadcasting
    angle_indices = np.abs(angles[:, None] - angles_ref).argmin(axis=1)

    # Gán khoảng cách vào r_list
    for i in range(len(angle_indices)):
        r_list[angle_indices[i]] = distances[i]

    # **Nội suy giá trị NaN để làm mượt**
    valid_r = r_list[~np.isnan(r_list)]
    for i in range(len(r_list)):
        if np.isnan(r_list[i]):
            r_list[i] = np.mean(valid_r[max(0, i-5): min(len(valid_r), i+5)])  # Trung bình cục bộ

    # **Tính bán kính trung bình từ 100 giá trị nhỏ nhất**
    first_120 = np.random.choice(valid_r[:80], 25, replace=False)  # Lấy ngẫu nhiên 50 giá trị từ giữa
    middle_50 = np.random.choice(valid_r[80:300], 120, replace=False)  # Lấy ngẫu nhiên 50 giá trị từ giữa
    last_10 = np.random.choice(valid_r[300:], 10, replace=False)  # Lấy ngẫu nhiên 50 giá trị từ giữa

    # Gộp tất cả vào một danh sách
    selected_values = np.concatenate([ middle_50,last_10])

    # Tính r_mean
    r_mean = np.median(np.sort(selected_values))

    # Debug số lượng góc có giá trị hợp lệ
    print(f"Số góc có giá trị hợp lệ: {np.count_nonzero(~np.isnan(r_list))} / 360")

    # Nội suy nếu còn thiếu
    valid_indices = np.where(~np.isnan(r_list))[0]
    valid_r_values = r_list[valid_indices]
    full_indices = np.arange(360)
    r_list = np.interp(full_indices, valid_indices, valid_r_values)

    # **Vẽ các đường tia**
    count_red = 0
    for angle in range(0, 360, 2):  # Giảm mật độ tia (mỗi 5 độ)
        theta = np.deg2rad(angle)
        r = r_list[angle]

        # Xác định màu sắc
        if 4< abs(r - r_mean):
            color = (0, 0, 255)  # Đỏ nếu bất thường
            count_red += 1  
        else:
            color = (0, 255, 0)  # Xanh nếu ổn

        # Xác định điểm kết thúc
        x_end, y_end = int(cx + r * np.cos(theta)), int(cy + r * np.sin(theta))

        # Vẽ đường tia
        cv2.line(output, (cx, cy), (x_end, y_end), color, 1)

    # Hiển thị số tia màu đỏ
    print(f"Số lượng tia bất thường (màu đỏ): {count_red}")

    time_end = time.time()
    print(f'Cycle time: {time_end - time_start:.4f} giây')

# # Hiển thị ảnh (tuỳ chọn)
    cv2.imshow("Result", output)
    cv2.waitKey(0)
# cv2.destroyAllWindows()

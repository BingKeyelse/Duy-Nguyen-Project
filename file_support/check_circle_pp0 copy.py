import cv2
import numpy as np
import time

# Đọc ảnh đầu vào
image = cv2.imread(r"picture\test_circle.png", cv2.IMREAD_GRAYSCALE)
while True:
    time_start=time.time()


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

    # Tạo mask để lấy biên của hình tròn
    mask = np.zeros_like(image)
    cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

    h, w = mask.shape

    # Tạo ảnh màu để vẽ kết quả
    output = cv2.cvtColor(mask.copy(), cv2.COLOR_GRAY2BGR)

    # Danh sách chứa các bán kính
    r_list = np.full(360, np.nan)  # Dùng NaN để đánh dấu góc chưa tìm thấy biên

    # Quét 360 độ
    for angle in range(0, 360):
        theta = np.deg2rad(angle)
        dx, dy = np.cos(theta), np.sin(theta)

        for r in range(min(h, w) // 1):
            x, y = int(cx + r * dx), int(cy + r * dy)

            # Nếu ra ngoài biên ảnh, dừng
            if x < 0 or x >= w or y < 0 or y >= h:
                break

            # Nếu gặp biên (pixel chuyển từ trắng sang đen)
            if mask[y, x] == 0:
                r_list[angle] = r
                break

    # Nội suy các góc không có giá trị
    valid_r = r_list[~np.isnan(r_list)]
    r_list = np.where(np.isnan(r_list), np.median(valid_r), r_list)

    # Tính bán kính trung bình từ 100 giá trị nhỏ nhất
    # r_mean = np.median(np.sort(valid_r)[:150])
    # Lấy các phần dữ liệu theo yêu cầu
    first_120 = np.random.choice(valid_r[:80], 25, replace=False)  # Lấy ngẫu nhiên 50 giá trị từ giữa
    middle_50 = np.random.choice(valid_r[80:300], 120, replace=False)  # Lấy ngẫu nhiên 50 giá trị từ giữa
    last_10 = np.random.choice(valid_r[300:], 10, replace=False)  # Lấy ngẫu nhiên 50 giá trị từ giữa

    # Gộp tất cả vào một danh sách
    selected_values = np.concatenate([ middle_50,last_10])

    # Tính r_mean
    r_mean = np.median(np.sort(selected_values))

    print(r_mean)

    # Khởi tạo biến đếm số tia màu đỏ
    count_red = 0  

    # Vẽ các đường tia với màu phù hợp
    for angle in range(0, 360,2):
        theta = np.deg2rad(angle)
        dx, dy = np.cos(theta), np.sin(theta)
        r = r_list[angle]

        # Xác định màu sắc
        if np.isnan(r):  
            color = (0, 0, 255)  # Màu đỏ cho vùng không có biên
            count_red += 1  
        else:
            # if 2< abs(r - r_mean) <6:
            if 4< abs(r - r_mean) :
                color = (0, 0, 255)  # Đỏ nếu bất thường
                count_red += 1  
            else:
                color = (0, 255, 0)  # Xanh nếu ổn

        # Xác định điểm kết thúc
        x_end, y_end = int(cx + r * dx), int(cy + r * dy)

        # Vẽ đường tia
        cv2.line(output, (cx, cy), (x_end, y_end), color, 1)

        # Nếu là NaN, vẽ thêm điểm đỏ tại vị trí này để dễ nhìn
        if np.isnan(r):
            cv2.circle(output, (x_end, y_end), 2, (0, 0, 255), -1)  

    # Hiển thị số tia màu đỏ
    print(f"Số lượng tia bất thường (màu đỏ): {count_red}")

    # Lưu ảnh kết quả
    # cv2.imwrite("output_image.png", output)

    time_end=time.time()

    print(f'Cycle time: {time_end-time_start}')


# # Hiển thị ảnh (tuỳ chọn)
# cv2.imshow("Mask", mask)
# cv2.imshow("Result", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

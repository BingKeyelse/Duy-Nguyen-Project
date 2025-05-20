import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread(r"picture\test_circle.png", cv2.IMREAD_GRAYSCALE)

# Kiểm tra xem ảnh có đọc được không
if image is None:
    print("Lỗi: Không thể đọc ảnh! Kiểm tra đường dẫn file.")
    exit()

# Làm mịn ảnh để giảm nhiễu
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Nhị phân hóa ảnh
_, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

# Tìm contour
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if not contours:
    print("Không tìm thấy contour nào!")
    exit()

# Lấy contour lớn nhất theo diện tích
largest_contour = max(contours, key=cv2.contourArea)

# Tạo mask chỉ chứa contour lớn nhất
mask = np.zeros_like(image)
cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

# Sử dụng distance transform để tính khoảng cách từ viền vào tâm
dist_transform = cv2.distanceTransform(mask, cv2.DIST_L2, 5)

# Tìm tâm bằng giá trị max trong distance transform
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(dist_transform)
center_x, center_y = max_loc  # Tâm hình tròn

# Duyệt 360 tia, lấy khoảng cách từ tâm ra viền
distances = []
for angle in range(0, 360, 2):  # Duyệt góc với bước 2° để nhanh hơn
    x = int(center_x + max_val * np.cos(np.radians(angle)))
    y = int(center_y + max_val * np.sin(np.radians(angle)))

    if 0 <= x < image.shape[1] and 0 <= y < image.shape[0]:
        distances.append(dist_transform[y, x])

# Tính độ lệch chuẩn để phát hiện vùng viền không đồng đều
mean_distance = np.mean(distances)
std_dev = np.std(distances)
threshold = mean_distance + 1.5 * std_dev

# Xác định vùng bất thường
outliers = [angle for angle, d in zip(range(0, 360, 2), distances) if d > threshold]

print(f"Độ dài trung bình: {mean_distance:.2f} pixels")
print(f"Góc bất thường: {outliers}")

# Vẽ kết quả
output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
for angle, d in zip(range(0, 360, 2), distances):
    x = int(center_x + d * np.cos(np.radians(angle)))
    y = int(center_y + d * np.sin(np.radians(angle)))

    color = (0, 255, 0)  # Xanh lá (bình thường)
    if angle in outliers:
        color = (0, 0, 255)  # Đỏ (bất thường)

    cv2.line(output, (center_x, center_y), (x, y), color, 1)

cv2.imshow("Detected Outliers", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

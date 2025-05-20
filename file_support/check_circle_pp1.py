import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh
image = cv2.imread(r"picture\test_circle.png", cv2.IMREAD_GRAYSCALE)

# Tiền xử lý ảnh để tìm hình tròn
_, mask = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Tìm các contours trong ảnh
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Chọn contour có diện tích lớn nhất
largest_contour = max(contours, key=cv2.contourArea)

# Fit hình tròn vào contour lớn nhất
(x, y), radius = cv2.minEnclosingCircle(largest_contour)
center_x, center_y, radius = int(x), int(y), int(radius)

# Duyệt 360 tia để lấy khoảng cách từ tâm ra viền
angles = np.arange(0, 360, 2)
distances = []

for angle in angles:
    x_end = int(center_x + radius * np.cos(np.radians(angle)))
    y_end = int(center_y + radius * np.sin(np.radians(angle)))
    
    line = cv2.line(np.zeros_like(mask), (center_x, center_y), (x_end, y_end), 255, 1)
    intersection = cv2.bitwise_and(mask, line)
    
    points = np.column_stack(np.where(intersection > 0))
    if len(points) > 0:
        dist = np.sqrt((points[-1][1] - center_x) ** 2 + (points[-1][0] - center_y) ** 2)
        distances.append(dist)
    else:
        distances.append(radius)

# Phát hiện bất thường dựa trên độ lệch chuẩn
mean_distance = np.mean(distances)
std_dev = np.std(distances)
threshold = mean_distance + 1.5 * std_dev
outliers = [angle for angle, d in zip(angles, distances) if d > threshold]

# Vẽ kết quả
output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
for angle, d in zip(angles, distances):
    x_end = int(center_x + d * np.cos(np.radians(angle)))
    y_end = int(center_y + d * np.sin(np.radians(angle)))
    color = (0, 255, 0) if angle not in outliers else (0, 0, 255)
    cv2.line(output, (center_x, center_y), (x_end, y_end), color, 1)

cv2.circle(output, (center_x, center_y), radius, (255, 0, 0), 2)
cv2.circle(output, (center_x, center_y), 3, (0, 255, 255), -1)

# Hiển thị kết quả
plt.figure(figsize=(6, 6))
plt.imshow(output)
plt.title("Detected Outliers")
plt.axis("off")
plt.show()

# In thông tin hình tròn và góc bất thường
print(f"Tâm: ({center_x}, {center_y}) - Bán kính: {radius}")
print(f"Góc bất thường: {outliers}")

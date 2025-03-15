import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread(r"picture\test_circle.png", cv2.IMREAD_GRAYSCALE)
# Tìm contour lớn nhất
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = max(contours, key=cv2.contourArea)

# Đơn giản hóa contour để giảm số điểm
epsilon = 0.01 * cv2.arcLength(contour, True)
approx_contour = cv2.approxPolyDP(contour, epsilon, True)

# Tính tâm và bán kính trung bình của các điểm
center_x = np.mean(approx_contour[:, 0, 0])
center_y = np.mean(approx_contour[:, 0, 1])
mean_radius = np.mean([np.linalg.norm((x - center_x, y - center_y)) for x, y in approx_contour[:, 0, :]])

print(f"Tâm: ({int(center_x)}, {int(center_y)}), Bán kính trung bình: {int(mean_radius)}")

# Kiểm tra sai lệch
output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
for point in approx_contour[:, 0, :]:  
    x, y = point
    distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    if abs(distance - mean_radius) > 5:  
        cv2.circle(output, (x, y), 3, (0, 0, 255), -1)  # Chấm đỏ

cv2.imshow("Contour Approximation", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

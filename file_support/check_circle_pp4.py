import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread(r"picture\test_circle.png", cv2.IMREAD_GRAYSCALE)
# Lấy contour chính
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = max(contours, key=cv2.contourArea)

# Tìm elip khớp với contour
ellipse = cv2.fitEllipse(contour)
(center_x, center_y), (major_axis, minor_axis), angle = ellipse

print(f"Tâm: ({int(center_x)}, {int(center_y)}), Trục lớn: {int(major_axis)}, Trục nhỏ: {int(minor_axis)}")
count=0

# Kiểm tra sai lệch
output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
for point in contour[:, 0, :]:  
    x, y = point
    distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    if abs(distance - (major_axis / 2)) > 15:  
        cv2.circle(output, (x, y), 3, (0, 0, 255), -1)  # Chấm đỏ
        count= count+1
print(f'count: {count}')
# Vẽ elip chuẩn
cv2.ellipse(output, ellipse, (0, 255, 0), 2)

cv2.imshow("Fit Ellipse", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

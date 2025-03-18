import cv2
import numpy as np

# Đọc ảnh đầu vào
image = cv2.imread(r"picture\test_circle.png", cv2.IMREAD_GRAYSCALE)

# Nhị phân hóa ảnh để lấy vùng hình tròn
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

## Tìm contour lớn nhất (hình tròn)
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if not contours:
    print("Không tìm thấy hình tròn trong ảnh.")
    exit()

largest_contour = max(contours, key=cv2.contourArea)

# Tạo mask để tô trắng phần bên trong hình tròn
mask = np.zeros_like(image)
cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)
# cv2.imwrite(r"picture\test_circle.png", mask)
cv2.imshow('aa',mask)
cv2.waitKey(0)
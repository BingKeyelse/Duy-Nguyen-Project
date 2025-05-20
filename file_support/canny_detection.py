import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread(r"picture\real_circle_canny.png", cv2.IMREAD_GRAYSCALE)

# Làm mờ ảnh bằng Gaussian Blur
blurred = cv2.GaussianBlur(image, (5,5), 1.4)

# Áp dụng Canny Edge Detection
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blurred, low_threshold, high_threshold)

# Hiển thị kết quả
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

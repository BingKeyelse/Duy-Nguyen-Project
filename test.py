import cv2
import numpy as np

# Đọc ảnh gốc và ảnh mẫu
image = cv2.imread('picture/test_cam1.png')
template = cv2.imread('picture/saved_sample.png')

# Resize ảnh về 50% kích thước ban đầu để tăng tốc độ matching
image = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2))
template = cv2.resize(template, (template.shape[1]//2, template.shape[0]//2))

# Chuyển ảnh sang grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Tạo mask để loại bỏ nền đen
_, mask = cv2.threshold(gray_template, 10, 255, cv2.THRESH_BINARY)

# Matching sử dụng template matching
result = cv2.matchTemplate(gray_img, gray_template, cv2.TM_CCOEFF_NORMED, mask=mask)

# Tìm vị trí matching tốt nhất
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Kiểm tra nếu matching trên 80%
threshold = 0.8  # Ngưỡng tối thiểu 80%
if max_val >= threshold:
    print(f"Matching found with confidence: {max_val:.2f}")

    # Vẽ hình chữ nhật quanh vùng matching
    h, w = gray_template.shape
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

    # Cắt ảnh vùng matching
    matched_region = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

    # Lưu ảnh vùng matching
    cv2.imwrite("matched_region.png", matched_region)

    # Hiển thị kết quả
    cv2.imshow("Matching Result", image)
    cv2.imshow("Matched Region", matched_region)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"No good match found. Best match confidence: {max_val:.2f}")

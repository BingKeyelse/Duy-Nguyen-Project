import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread(r"picture\test_circle.png", cv2.IMREAD_GRAYSCALE)

# Phát hiện hình tròn với Hough Transform
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                            param1=30, param2=20, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.uint16(np.around(circles))
    center_x, center_y, detected_radius = circles[0][0]  # Lấy tâm và bán kính

    print(f"Tâm: ({center_x}, {center_y}), Bán kính phát hiện: {detected_radius}")

    # Tạo mask hình tròn để so sánh với hình tròn thực tế
    mask = np.zeros_like(image)
    cv2.circle(mask, (center_x, center_y), detected_radius, 255, thickness=1)

    # Xác định viền thực tế từ ảnh
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    actual_contour = max(contours, key=cv2.contourArea)

    # Tạo ảnh màu để hiển thị
    output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # So sánh viền thực tế với viền lý tưởng
    for point in actual_contour[:, 0, :]:  
        x, y = point
        distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        if abs(distance - detected_radius) > 5:  # Nếu sai lệch > 5 pixel
            cv2.circle(output, (x, y), 2, (0, 0, 255), -1)  # Chấm đỏ

    # Hiển thị kết quả
    cv2.imshow("Detected Circle with Anomalies", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

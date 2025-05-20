import cv2
import numpy as np
import math
import time
# /home/pronics/miniconda3/envs/lib_DuyNguyen/bin/python /home/pronics/Desktop/Duy-Nguyen-Project/file_support/code_check_change_bavia.py

import cv2
import numpy as np
import time

def detect_bavia_by_angle(binary_mask, image):
    start = time.time()

    # Resize nếu cần
    if binary_mask.shape[:2] != image.shape[:2]:
        image = cv2.resize(image, (binary_mask.shape[1], binary_mask.shape[0]))
    result_image = image.copy()

    # Tìm contour lớn nhất
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if not contours:
        print("❌ Không tìm thấy contour nào.")
        return result_image

    largest_contour = max(contours, key=cv2.contourArea)
    contour = largest_contour[:, 0, :].astype(np.float32)  # (N, 2)

    if len(contour) < 10:
        print("⚠️ Contour quá nhỏ.")
        return result_image

    step = max(1, int(len(contour) / 180))
    print(f'Gia tri {step}')
    idx = np.arange(step, len(contour) - step,step)
    # print(idx)
    p0 = contour[idx - step]
    p1 = contour[idx]
    p2 = contour[idx + step]

    # Vector hóa
    v1 = p1 - p0
    v2 = p2 - p1

    v1_norm = np.linalg.norm(v1, axis=1, keepdims=True)
    v2_norm = np.linalg.norm(v2, axis=1, keepdims=True)

    unit_v1 = v1 / np.clip(v1_norm, 1e-8, None)
    unit_v2 = v2 / np.clip(v2_norm, 1e-8, None)

    dot_products = np.sum(unit_v1 * unit_v2, axis=1)
    dot_products = np.clip(dot_products, -1.0, 1.0)
    angles_deg = np.degrees(np.arccos(dot_products))

    # Tìm các điểm góc nhọn (nghi ngờ bavia)
    spike_mask = angles_deg >5  # Tùy chỉnh ngưỡng góc
    spike_points = p1[spike_mask].astype(int)

    for pt in spike_points:
        cv2.circle(result_image, tuple(pt), 3, (0, 0, 255), -1)

    cv2.drawContours(result_image, [largest_contour], -1, (0, 255, 0), 1)
    cv2.imshow("Bavia Detect", result_image)
    print(f"🟢 Số điểm nghi ngờ bavia: {len(spike_points)}")

    fps = 1.0 / (time.time() - start)
    print(f"🎯 FPS: {fps:.2f}")
    return result_image

def angle_between(v1, v2):
    # Tính góc giữa hai vector (trả về độ)
    unit_v1 = v1 / np.linalg.norm(v1)
    unit_v2 = v2 / np.linalg.norm(v2)
    dot = np.clip(np.dot(unit_v1, unit_v2), -1.0, 1.0)
    angle_rad = np.arccos(dot)
    return np.degrees(angle_rad)

def curvature(p0, p1, p2):
    v1 = p1 - p0
    v2 = p2 - p1
    angle = angle_between(v1, v2)
    return angle  # càng nhỏ thì càng "gấp khúc" (bavia)
image = cv2.imread("data_check/test_cam1.png")
binary = cv2.imread("data_check/test_circle.png", 0)

result = detect_bavia_by_angle(binary, image)  # Bạn có thể chỉnh ngưỡng góc
# cv2.imwrite("result_bavia_angle.png", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

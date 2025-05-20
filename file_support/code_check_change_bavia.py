import cv2
import numpy as np
import math
import time
# /home/pronics/miniconda3/envs/lib_DuyNguyen/bin/python /home/pronics/Desktop/Duy-Nguyen-Project/file_support/code_check_change_bavia.py

def detect_bavia_by_angle(binary_mask, image):
    start=time.time()
    result_image = image.copy()

    # Resize nếu cần
    if binary_mask.shape[:2] != image.shape[:2]:
        result_image = cv2.resize(result_image, (binary_mask.shape[1], binary_mask.shape[0]))

    # Làm sạch bằng morphology
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    # clean_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_CLOSE, kernel)

    # Tìm contour
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    haha=result_image.copy()

    for contour in contours:

        contour = contour[:, 0, :]  # Remove extra dimension
        step = int(len(contour)/180)
        spikes = []

        for i in range(step, len(contour)-step,step):
            p0 = contour[i-step]
            p1 = contour[i]
            p2 = contour[i+step]

            # Tính góc giữa hai vector (p0 -> p1) và (p1 -> p2)
            v1 = p1 - p0
            v2 = p2 - p1

            angle = angle_between(v1, v2)
            # if angle > angle_threshold:
            if curvature(p0, p1, p2) >5:  # góc nhỏ hơn tức là "nhọn"

                spikes.append(p1)
                cv2.circle(result_image, tuple(p1), 3, (0,0,255), -1)  # Đánh dấu điểm nghi ngờ
                # Vẽ đường thẳng nối giữa 2 điểm liên tiếp (p1 và p2)
                cv2.line(haha, tuple(p1), tuple(contour[i+step]), (0, 0, 255), 2)
        cv2.imshow('1', haha)


        # Vẽ contour
        cv2.drawContours(result_image, [contour], -1, (0,255,0), 1)
        cv2.imshow('2', result_image)


        print(f"🔍 Số điểm nghi ngờ bavia: {len(spikes)}")
        if len(spikes) > 0:
            print("⚠️ Phát hiện bavia theo góc thay đổi")
    fps= (1/(time.time()-start))
    print(f'Gias tri fps la: {fps:.3f}')
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

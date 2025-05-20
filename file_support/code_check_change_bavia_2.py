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
    contour = largest_contour[:, 0, :].astype(np.float32)  # (N, 2) và float32 cho nhanh

    if len(contour) < 10:
        print("⚠️ Contour quá nhỏ.")
        return result_image

    step = max(1, len(contour) // 180)
    idx = np.arange(step, len(contour) - step, step)

    p0 = contour[idx - step]
    p1 = contour[idx]
    p2 = contour[idx + step]

    # Vector hóa
    v1 = p1 - p0
    v2 = p2 - p1

    v1_norm = np.linalg.norm(v1, axis=1, keepdims=True)
    v2_norm = np.linalg.norm(v2, axis=1, keepdims=True)

    # Tránh chia 0
    v1_norm = np.maximum(v1_norm, 1e-8)
    v2_norm = np.maximum(v2_norm, 1e-8)

    unit_v1 = v1 / v1_norm
    unit_v2 = v2 / v2_norm

    dot_products = np.sum(unit_v1 * unit_v2, axis=1)
    dot_products = np.clip(dot_products, -1.0, 1.0)
    angles_deg = np.degrees(np.arccos(dot_products))

    # Tìm các điểm nghi ngờ
    spike_mask = angles_deg > 5
    spike_points = p1[spike_mask].astype(int)

    spike_lines = zip(p1[spike_mask], p2[spike_mask])  # Vẽ từ p1 đến p2
    haha=result_image.copy()
    # Vẽ điểm + đường
    for pt1, pt2 in spike_lines:
        pt1 = tuple(pt1.astype(int))
        pt2 = tuple(pt2.astype(int))
        cv2.circle(haha, pt1, 3, (0, 0, 255), -1)
        cv2.line(haha, pt1, pt2, (0, 0, 255), 1)  # vẽ line đỏ
# ======
    cv2.drawContours(result_image, [largest_contour], -1, (0, 255, 0), 1)
    cv2.imshow("Detect", haha)
    print(f"🟢 Số điểm nghi ngờ bavia: {len(spike_points)}")
    print(f"🎯 FPS: {1.0 / (time.time() - start):.2f}")
    return result_image

# === DEMO TEST ===
if __name__ == "__main__":
    image = cv2.imread("data_check/test_cam1.png")
    binary = cv2.imread("data_check/test_circle.png", 0)

    result = detect_bavia_by_angle(binary, image)
    cv2.imshow("Bavia Detect", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

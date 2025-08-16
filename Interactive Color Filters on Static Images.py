import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    filtered = image.copy()
    if filter_type == "red_tint":
        filtered[:, :, 2] = np.clip(filtered[:, :, 2] * 1.5, 0, 255)
    elif filter_type == "blue_tint":
        filtered[:, :, 0] = np.clip(filtered[:, :, 0] * 1.5, 0, 255)
    elif filter_type == "green_tint":
        filtered[:, :, 1] = np.clip(filtered[:, :, 1] * 1.5, 0, 255)
    elif filter_type == "increase_red":
        filtered[:, :, 2] = np.clip(filtered[:, :, 2] + 50, 0, 255)
    elif filter_type == "decrease_blue":
        filtered[:, :, 0] = np.clip(filtered[:, :, 0] - 50, 0, 255)
    return filtered

image = cv2.imread("example.jpg")
if image is None:
    print("Error: Image not found!")
else:
    filter_type = "original"
    print("Press keys: r=Red, b=Blue, g=Green, i=+Red, c=-Blue, q=Quit")
    
    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("Filtered Image", filtered_image)
        key = cv2.waitKey(0) & 0xFF
        
        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord('c'):
            filter_type = "decrease_blue"
        elif key == ord('q'):
            break 

    cv2.destroyAllWindows()
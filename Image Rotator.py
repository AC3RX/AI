import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Test.png')
if image is None:
    print("Image not found. Make sure 'example.jpg' is in the same folder.")
    exit()

direction = input("Enter rotation direction (right, left, upside down): ").lower()
angle = {"right": -90, "left": 90, "upside down": 180}.get(direction, 0)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

brightness_level = input("Choose brightness (low, normal, high): ").lower()
brightness = {"low": 20, "normal": 50, "high": 100}.get(brightness_level, 50)
bright = cv2.add(rotated, np.ones(rotated.shape, dtype="uint8") * brightness)

contrast_level = input("Choose contrast (low, normal, high): ").lower()
contrast = {"low": 0.5, "normal": 1.0, "high": 1.5}.get(contrast_level, 1.0)
contrasted = cv2.convertScaleAbs(bright, alpha=contrast, beta=0)

blur_input = input("Apply blur? (yes or no): ").lower()
if blur_input == "yes":
    blurred = cv2.GaussianBlur(contrasted, (9, 9), 0)
else:
    blurred = contrasted

effect = input("Choose effect (xray, grayscale, edges, none): ").lower()
if effect == "xray":
    final = cv2.bitwise_not(blurred)
    final = cv2.cvtColor(final, cv2.COLOR_BGR2RGB)
elif effect == "grayscale":
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    final = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
elif effect == "edges":
    edges = cv2.Canny(blurred, 100, 200)
    final = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
else:
    final = cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB)

plt.imshow(final)
plt.title("Final Image")
plt.axis('off')
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('example.jpg')
if image is None:
    image = np.ones((600, 800, 3), dtype=np.uint8) * 255
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

h, w = image.shape[:2]

rect_start = (30, 30)
rect_end = (130, 130)
cv2.rectangle(image, rect_start, rect_end, (0, 255, 255), 2)

center = ((rect_start[0] + rect_end[0]) // 2, (rect_start[1] + rect_end[1]) // 2)
cv2.circle(image, center, 7, (0, 255, 255), -1)

line_end = (w - 100, h - 100)
cv2.line(image, center, line_end, (0, 255, 0), 2)

fig, ax = plt.subplots(figsize=(10, 7))
ax.imshow(image)
ax.axis('off')

ax.set_title('Annotated Image with Regions, Centers, and Bi-Directional Height Arrow', fontsize=12)

ax.text(center[0]-30, center[1]-10, 'Center', color='cyan', fontsize=10, weight='bold')

arrow_x = w - 40
arrow_y_start = 50
arrow_y_end = h - 50
ax.annotate('', xy=(arrow_x, arrow_y_end), xytext=(arrow_x, arrow_y_start),
            arrowprops=dict(arrowstyle='<->', color='yellow', linewidth=2))
height_px = arrow_y_end - arrow_y_start
ax.text(arrow_x - 60, h//2, f'Height: {height_px}px', color='yellow', fontsize=10, rotation=90,
        verticalalignment='center', weight='bold')

plt.show()


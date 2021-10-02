import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = "IMG_20200721_183045.jpg"
img = cv2.imread(file)

t1 = 50
t2 = 100
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, t1, t2)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 20, maxLineGap=150, minLineLength=1500)

theta = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    if abs(x1-x2) != 0 and abs((y2-y1)/(x2-x1)) < np.tan(np.pi/6) and y1 < img.shape[0]*0.9 and y2 < img.shape[0]*0.9 \
            and y1 > img.shape[0]*0.1 and y2 > img.shape[0]*0.1:

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 20)
        cv2.circle(img, (x1,y1), 30, (0, 255, 0),20)
        cv2.circle(img, (x2, y2), 30, (0, 255, 0),20)
        cv2.circle(img, (int(np.mean((x1, x2), None)), int(np.mean((y1, y2), None))), 10, (0, 0, 255), 20)
        theta.append(np.arctan((y2-y1)/(x2-x1))*180/np.pi)


meantheta = np.mean(theta, None)
stdtheta = np.std(theta)
print(meantheta, stdtheta)
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Theta: ' + str(round(meantheta,2)) + " +/- " + str(round(stdtheta,2)))
# plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(255-edges, cmap='gray')
plt.title('Edge Image')
# plt.xticks([]), plt.yticks([])

plt.show()
print("Completed")
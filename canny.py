import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread('mario.jpg',cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

edges = cv2.Canny(img,100,200)
#edges = ~edges

edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.savefig('saved_figure.png')

cv2.imwrite('image.png',edges)

img2 = cv2.imread('mario.jpg')


sub = cv2.subtract(img, edges)

sub = cv2.cvtColor(sub, cv2.COLOR_BGR2RGB)

cv2.imwrite('image2.png',sub)

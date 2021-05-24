import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

def scale_contour(cnt, scale):
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cnt_norm = cnt
    cnt_scaled = cnt_norm * scale
    cnt_scaled = cnt_scaled
    cnt_scaled = cnt_scaled.astype(np.int32)

    return cnt_scaled


im = Image.open('mario.jpg')

org_size = im.size
pixelate_lvl = 3

# scale it down
im = im.resize(
    size=(org_size[0] // pixelate_lvl, org_size[1] // pixelate_lvl),
    resample=0)

im.save('pixelated.png')

img = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)

# Converting image to grayscale
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding and getting contours from the image
ret, thresh = cv2.threshold(imgray, 20, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# and scale it up to get pixelate effect
im = im.resize(org_size, resample=0)

img = cv2.resize(img, (0,0), fx=3, fy=3, interpolation=cv2.INTER_NEAREST)

cnt_scaled = scale_contour(contours[0], 3)

im_copy = img.copy()
cv2.drawContours(im_copy, [cnt_scaled], 0, (0, 255, 0), 2,lineType = cv2.LINE_8)
cv2.imshow('test',im_copy)
cv2.imwrite('result2.png',im_copy)   



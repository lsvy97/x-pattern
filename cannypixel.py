import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

im = Image.open('mario.jpg')

org_size = im.size
pixelate_lvl = 3

# scale it down
im = im.resize(
    size=(org_size[0] // pixelate_lvl, org_size[1] // pixelate_lvl),
    resample=0)

im.save('pixelated.png')

img = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)

edges = cv2.Canny(img,100,200)
#edges = ~edges

edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)

cv2.imwrite('image.png',edges)

sub = cv2.subtract(img, edges)

cv2.imwrite('image2.png',sub)

sub = cv2.cvtColor(sub, cv2.COLOR_BGR2RGB)

im = Image.fromarray(sub)



# and scale it up to get pixelate effect
im = im.resize(org_size, resample=0)
    
im.save('result.png')
im.show()

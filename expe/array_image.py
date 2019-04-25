#!/usr/bin/env python3

from PIL import Image
import numpy as np

w,h = 100,50

a = np.full((720,1080,3), [255,0,0])
b = np.full((h,w,3), [255,255,0])

x,y = 10,10

a[x:x+b.shape[0], y:y+b.shape[1]] = b

img = Image.fromarray(np.uint8(a))
img.show()

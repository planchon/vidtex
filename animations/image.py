import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from animations.animation import Animation

import cv2

class Image(Animation):
    # an image is not animated by default, its just render the image. The animation class
    # is responsible for the scaling and position

    def __init__(self, image, **kwargs):
        print("animation -> image")
        self.image = cv2.imread(image, mode='RGB')
        
    def render(self, t):
        return self.image

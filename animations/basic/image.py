import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from animations.animation import *
from constants.constants import *

import cv2

class StillImage(Animation):
	# an image is not animated by default, its just render the image.
	def __init__(self, image):
		super().__init__()
		if os.path.exists(image):
			self.image = cv2.imread(image)
		else:
			print("image dont exists")
	
	def render(self, t):
		return self.image
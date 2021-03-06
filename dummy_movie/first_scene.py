import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from scene.scene import Scene

import traceback

# from animations.basic.write import *
from animations.basic.fillScreen import *
from animations.basic.image import *
from animations.basic.solid import *
from animations.basic.video import *

from animations.planchonio.squelette import *

class FirstScene(Scene):
	def __init__(self):
		super().__init__()
		 
	def prepare(self):
		self.add_to_timeline(FillScreen([255, 255, 0]), 0, 60)
		
		self.add_to_timeline(Video("dummy_movie/cut.mp4", (0, 120)).set_half_video(True), 0, 120, z_index=-1)
		
		self.add_to_timeline(Solid((100,500), (500, 500), [255,0,255]), 60, 120)
		self.add_to_timeline(StillImage("dummy_movie/testimage.jpg"), 0, 60, z_index=1)
		self.add_to_timeline(Squelette((100, 100)), 0, 60, z_index=2)
		
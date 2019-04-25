import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from scene.scene import Scene

from animations.write import *
from animations.fillScreen import *
from animations.image import *
from animations.solid import *
from animations.video import *

class FirstScene(Scene):
	def __init__(self):
		super().__init__()
		 
	def prepare(self):
		self.add_to_timeline(FillScreen([255, 255, 0]), 0, 60)
		video = Video("dummy_movie/dummy_video.mp4", (120, 180))
		video.set_half_video(True)
		self.add_to_timeline(video, 10, 60)
		self.add_to_timeline(Solid((100,500), (500, 500), [255,0,255]), 30, 60)
		self.add_to_timeline(StillImage("dummy_movie/testimage.jpg"), 0, 60, z_index=1)

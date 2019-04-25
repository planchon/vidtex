import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from scene.scene import Scene
from animations.image import *

class TestScene(Scene):
	def __init__(self):
		super().__init__()
		 
	def prepare(self):
		# self.add_to_timeline(FillScreen([255, 255, 0]), 0, 10)
		# self.add_to_timeline(Video("dummy_movie/dummy_video.mp4", (0, 60)), 10, 60)
		# self.add_to_timeline(Solid((100,500), (500, 500), [255,0,255]), 30, 60)
		print(os.getcwd())
		self.add_to_timeline(Image("../dummy_movie/testimage.jpg"), 0, 60)
		print("test after")	
		
def main():
	ts = FirstScene()

if __name__ == '__main__':
	main()
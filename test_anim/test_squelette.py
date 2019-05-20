import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from scene.scene import Scene
from animations.planchonio.squelette import *
from PIL import Image

class TestScene(Scene):
	def __init__(self):
		super().__init__()
		 
	def prepare(self):
		# self.add_to_timeline(FillScreen([255, 255, 0]), 0, 10)
		# self.add_to_timeline(Video("dummy_movie/dummy_video.mp4", (0, 60)), 10, 60)
		# self.add_to_timeline(Solid((100,500), (500, 500), [255,0,255]), 30, 60)
		print(os.getcwd())
		self.add_to_timeline(Squelette((1280 // 2, 720)), 0, 60)

def main():
	ts = TestScene()
	image = ts.render(0)
	Image.fromarray(np.uint8(image)).show()

if __name__ == '__main__':
	main()
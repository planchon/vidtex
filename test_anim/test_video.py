import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from animations.video import *

from PIL import Image

def main():
	video = Video("test_anim/cut.mp4", (0,1))
	im = Image.fromarray(np.uint8(video.render(15)))
	im.show()

if __name__ == '__main__':
	main()
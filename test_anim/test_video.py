import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from animations.video import *

from PIL import Image

def main():
	video = Video("test_anim/dummy_video.mp4", (0,1))
	video.set_half_video(True)
	im = Image.fromarray(np.uint8(video.render(1)))
	im.show()

if __name__ == '__main__':
	main()
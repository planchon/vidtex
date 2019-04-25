import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from animations.image import *

def main():
	image = Image("../dummy_movie/testimage.jpg")
	print(image.render(10))

if __name__ == '__main__':
	main()
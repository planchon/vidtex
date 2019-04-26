import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from animations.write import *

def main():
	write = Write("test")

if __name__ == '__main__':
	main()
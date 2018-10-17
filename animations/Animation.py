import sys, os, constants
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from render.Container import Container

class Animation(Container):
    def __init__(self):
        print("Dans animation")

    def play(self):
        pass

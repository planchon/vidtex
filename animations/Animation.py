import sys, os, constants
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from render.Container import Container

class Animation(Container):
    duration = 0 # infini
    
    def __init__(self):
        print("Dans animation")

    def play(self):
        print("je suis play (container)")

    def time(self, time):
        self.duration = time

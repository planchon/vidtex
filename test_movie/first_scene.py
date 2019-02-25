import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from scene.Scene import Scene

from animations.Write import *
from animations.FillScreen import *

class FirstScene(Scene):
    def __init__(self):
        print("dans la premiere scene")
        Scene.__init__(self)

    def prepare(self):
        self.add_to_timeline(FillScreen("col"), 0, 10)
        self.add_to_timeline(Write("test"), 0, 10)

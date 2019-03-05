import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from scene.scene import Scene

from animations.write import *
from animations.fillScreen import *
from animations.image import *

class FirstScene(Scene):
    def __init__(self):
        super().__init__()
         
    def prepare(self):
        self.add_to_timeline(FillScreen([255, 255, 0]), 0, 60)        
        self.add_to_timeline(FillScreen([255, 0, 0]), 60, 120)        

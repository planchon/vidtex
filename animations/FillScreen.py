import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from animations.Animation import Animation

class FillScreen(Animation):
    def __init__(self, color, **kwargs):
        print("animation -> fillScreen")
    
    def play(self):
        pass

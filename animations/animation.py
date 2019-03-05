import sys, os, constants
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

class Animation():
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0

    def render(self):
        pass
        
    # change the position of the animation 
    def at(self, x, y):
        self.pos_x = x
        self.pos_y = y

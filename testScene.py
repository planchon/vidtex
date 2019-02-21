from scene.Scene import Scene
from animations.Write import Write
from animations.FillScreen import FillScreen

class Test(Scene):
    def render(self):
        FillScreen((255, 255, 255)).time(2)

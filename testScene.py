from scene.Scene import Scene
from animations.Write import Write

class Test(Scene):
    def render(self):
        Write("teste")

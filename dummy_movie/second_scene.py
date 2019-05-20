import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from scene.scene import Scene

from animations.basic.write import Write

class SecondScene(Scene):
    def __init__(self):
        print("dans la seconde scene")
        Scene.__init__(self)

    def prepare(self):
        self.add_to_timeline(Write("test"), 0, 10)

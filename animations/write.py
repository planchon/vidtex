import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from animations.animation import Animation
from latex.texGenerator  import TexGenerator

class Write(Animation):
    buffer = []
    
    def __init__(self, text, **kwargs):
        # latexRender = TexGenerator(text).finalFile
        # points = SVGHandler(latexRender)
        print("animation -> write")
        
    def animate(self, t):
        #on fait l'animation du texte, pour l'instant que le rendering
        pass
        
    def render(self, t):
        return self.animate(t)

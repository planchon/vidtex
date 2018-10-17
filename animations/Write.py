import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from animations.Animation import Animation
from render.TexGenerator  import TexGenerator

class Write(Animation):
    def __init__(self, text, **kwargs):
        latexRender = TexGenerator("text")

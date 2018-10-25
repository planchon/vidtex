import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from animations.Animation import Animation
from latex.TexGenerator  import TexGenerator
from render.SvgHandler import SVGHandler

class Write(Animation):
    def __init__(self, text, **kwargs):
        latexRender = TexGenerator(text).finalFile
        points = SVGHandler(latexRender)
    

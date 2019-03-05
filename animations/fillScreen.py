import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

import numpy as np

from animations.animation import Animation
from constants.constants import *

class FillScreen(Animation):
    def __init__(self, color):
        super().__init__()
        self.buffer = np.full(np.insert(FRAME_DIMENSION, 2, 3), color)
        
    def render(self, t):
        return self.buffer

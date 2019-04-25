import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

import numpy as np

from animations.animation import Animation
from constants.constants import *

class Solid(Animation):
    def __init__(self, shape, pos, color):
        super().__init__()
        self.buffer = np.full(np.insert(shape, 2, 3), color)
        self.at(pos[0], pos[1])

    def render(self, t):
        return self.buffer

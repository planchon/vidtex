import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from PIL import Image, ImageDraw, ImageFont
import numpy as np

from animations.animation import *

# creer le squelette de l'image (bordure)
# fs = bordure sur tout le screen
# hsr = bordure sur le cote droit
# hsl = bordure sur le cote gauche
class Squelette(Animation):
    def __init__(self, shape, disposition="fs"):
        super().__init__()
        self.scale = 2
        self.width  = shape[0]
        self.height = shape[1]
        self.disposition = disposition
        self.buffer = []

        self.font = ImageFont.truetype("animations/planchonio/UbuntuMono-Regular.ttf", 12 * self.scale)
        self.font_shape = self.font.getsize(" ")
        self.hmodulo = (self.height % self.font_shape[1])
        self.wmodulo = (self.width % self.font_shape[0])
        self.width = self.width - self.wmodulo
        self.height = self.height - self.hmodulo - (self.font_shape[1] // 2) + 1
        self.shape = (self.width, self.height)
        self.image = Image.new("RGB", self.shape, (0,0,0))        
        self.drawing = ImageDraw.Draw(self.image)
        self.create_text_bordure()

        self.buffer = np.array(self.image)

    def create_text_bordure(self):
        yoffset = - self.font_shape[1] // 2 + 1
        self.drawing.text((0,0 + yoffset), "+" + "-" * (self.width // self.font_shape[0] - 2) + "+\n", (255, 255, 255), font=self.font)
        h = self.height // self.font_shape[1]
        for i in range(1, h):
            self.drawing.text((0, i * self.font_shape[1] + yoffset), "|" + " " * (self.width // self.font_shape[0] - 2) + "|\n", (255, 255, 255), font=self.font)
        self.drawing.text((0, self.font_shape[1] * h + yoffset), "+" + "-" * (self.width // self.font_shape[0] - 2) + "+\n", (255, 255, 255), font=self.font)

    def render(self, t):
        return self.buffer
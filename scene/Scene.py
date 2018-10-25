import numpy as np

from render.Container import Container

class Scene(Container):
    def __init__(self, **kargs):
        self.frames = [[[255,0,255] for i in range(720)] for j in range(1080)]
        self.frames = self.convertToUInt8Frame(self.frames)
        self.openPipe()
        for i in range(60):
            self.addFrameToMovie(self.frames)
        self.closePipe()
        
        #self.render()

    def render(self):
        pass
   
    


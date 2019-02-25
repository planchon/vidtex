import numpy as np

from render.Container import Container
from timeline.Timeline import Timeline

class Scene(Container):
    def __init__(self, **kargs):
        self.tl = Timeline()
        self.prepare()

    def add_to_timeline(self, anim, start, end):
        return self.tl.add_object(anim, start, end, 0)

    def prepare(self):
        pass
    
    def render(self):
        pass

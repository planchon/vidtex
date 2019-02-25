import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from timeline.Timeline import *

class Movie(object):
    tl = Timeline()
    
    def __init__(self):
        print("dans le movie CLASS")
        self.prepare()
        self.init_all_scene()
    
    def render(self):
        pass

    def prepare(self):
        pass
    
    def init_all_scene(self):
        timeline = self.tl.timeline_object.items()
        for scene in timeline:
            print(timeline, id(timeline))
            print(scene[1])
            scene[1]()

    # ajoute une scene a la tl global, retourne son id (pour les transition par exemple (ou les effets et post))
    def add_to_timeline(self, scene, start, end):
        return self.tl.add_object(scene, start, end, 0)

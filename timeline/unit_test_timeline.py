# coding: utf-8
from timeline import *

if __name__ == "__main__":
    tl = Timeline()

    tl.add_object("fillScreen", 10, 25, 1)
    tl.add_object("write (anim)", 15, 20, 1)
    tl.add_object("write", 25, 30, 1)
    tl.add_object("image", 20, 35, 1)
    tl.add_object("black", 0, 50, 0)
    
    anims = tl.get_all_animation_at(34)
    
    for anim in anims:
        print(tl.timeline_object[anim[0]])

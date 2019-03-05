import numpy as np

from timeline.timeline import Timeline
from constants.constants import *

class Scene():
    def __init__(self):
        self.tl = Timeline()
        self.prepare()
        self.frame_dimension = FRAME_DIMENSION
        self.scene_duration = self.tl.get_timeline_duration()
        self.frame_buffer = []
        
    def add_to_timeline(self, anim, start, end):
        return self.tl.add_object(anim, start, end, 0)

    def prepare(self):
        pass

    def clip_animation_into_frame_buffer(self, x, y, animation):
        tx = x
        ty = y
        bx = tx + animation.shape[0]
        by = ty + animation.shape[1]
        self.frame_buffer[tx:bx, ty:by] = animation
        
    # t in local time
    def render(self, t):
        all_animation_at_time = self.tl.get_all_animation_at(t)
        self.frame_buffer = np.zeros(np.insert(self.frame_dimension, 2, 3))
        for anim in all_animation_at_time:
            animation_buffer = anim["animation"].render(t - anim["start"])
            self.clip_animation_into_frame_buffer(anim["animation"].pos_x, anim["animation"].pos_y, animation_buffer)
        return self.frame_buffer
    

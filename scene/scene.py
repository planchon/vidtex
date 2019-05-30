import numpy as np

import sys
import cv2
import traceback

from timeline.timeline import Timeline
from constants.constants import *

from PIL import Image

class Scene():
	def __init__(self):
		
		self.CONFIG = {
			'frame_dimension': FRAME_DIMENSION,
		}

		self.tl = Timeline()
		try:
			self.prepare()
		except Exception:
			print("----- ERROR : SCENE_PREPARE ----- \n")
			traceback.print_exc()
			print("----- ERROR : SCENE_PREPARE -----")
			sys.exit()

		self.CONFIG["duration"] = self.tl.get_timeline_duration()
		self.buffer = []
		
	def add_to_timeline(self, anim, start, end, z_index=0):
		animation_scene_properties = anim.get_properties()
		print(animation_scene_properties)
		self.CONFIG = {**self.CONFIG, **animation_scene_properties}
		return self.tl.add_object(anim, start, end, z_index)

	def prepare(self):
		pass

	def clip_animation_into_frame_buffer(self, x, y, animation):
		self.buffer[x:x+animation.shape[0], y:y+animation.shape[1]] = animation

	# t in local time
	def render(self, t):
		all_animation_at_time = self.tl.get_all_animation_at(t)
		all_animation_at_time = sorted(all_animation_at_time, key=lambda x : x["pos"])
		self.buffer = np.full(np.insert(self.CONFIG["frame_dimension"], 2, 3), [0 ,0 ,0])
		for anim in all_animation_at_time:
			animation_buffer = anim["animation"].render(t - anim["start"])
			self.clip_animation_into_frame_buffer(anim["animation"].pos_x, anim["animation"].pos_y, animation_buffer)
		return self.buffer

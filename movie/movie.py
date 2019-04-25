import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

import subprocess as sp
import numpy as np
from tqdm import tqdm
import time 

from timeline.timeline import *
from constants.constants import *

class Movie(object):
    def __init__(self, frame_dimension=(1280,720), frame_rate=60):
        self.render_location = "/home/paul/psVidTex/out/test.mp4"
        self.tl = Timeline()
        self.frame_dimension = (frame_dimension[1], frame_dimension[0])
        self.frame_rate = frame_rate
        self.prepare()
        self.this_frame_buffer = []
        self.open_pipe()
        self.render()
        self.close_pipe()

    # go in the scene, do all the animation render, clip the animation render and repeat
    # pour l'instant les scenes ne se supperposent pas.
    def render(self):
        # main render loop
        print("rendering: {0} frames for {1} secondes".format(self.get_movie_duration(), self.get_movie_duration("secondes")))
        debut = time.time()
        for t in tqdm(range(self.get_movie_duration())):    
            self.this_frame_buffer = np.full(np.insert(self.frame_dimension, 2, 3), [255, 0, 0])
            scene_to_render = self.tl.get_all_animation_at(t)
            for scene in scene_to_render:
                # we do the render of the animation and clip the render to the the frame, then send the frame to ffmpeg
                self.this_frame_buffer = scene["animation"].render(t - scene["start"])

            # add the frame to the video
            self.add_frame_to_video()
        end = time.time()
        print("render finished in %fs, movie in : %s" % ((end - debut),self.render_location))
    
    def get_movie_duration(self, dtype="frames"):
        if dtype == "frames":
            return self.tl.get_timeline_duration()
        if dtype == "secondes":
            return self.tl.get_timeline_duration() / self.frame_rate
    
    # method used in movie subobject, called to init the scene
    def prepare(self):
        pass
            
    def open_pipe(self):
        command = [
            "ffmpeg",
            "-y", #overwrite last video if as the same name
            "-f", "rawvideo", #format
            "-vcodec", "rawvideo",
            "-s", "{0}x{1}".format(FRAME_DIMENSION[1], FRAME_DIMENSION[0]),
            "-pix_fmt", "rgb24",
            "-r", str(FRAME_RATE),
            "-i", "-", # work with pipe
            "-an", # no audio
            "-vcodec", "libx264",
            self.render_location
        ]

        self.pipe = sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)

    # push the frame in the ffmpeg pipe to add to the video
    def add_frame_to_video(self):
        self.pipe.stdin.write(np.uint8(self.this_frame_buffer).tostring())

    # close the pipe to finish the movie
    def close_pipe(self):
        self.pipe.stdin.close()
        self.pipe.wait()
            
    # ajoute une scene a la tl global, retourne son id (pour les transition par exemple (ou les effets et post))
    def add_to_timeline(self, scene, start, end, dtype="frames"):
        if dtype == "secondes":
            return self.tl.add_object(scene, start * FRAME_RATE, end * FRAME_RATE, 0)
        else:
            return self.tl.add_object(scene, start, end, 0)

#coding: utf8

import numpy as np
import subprocess as sp
import os

# Je suis la seule class qui peut emetre une image
class Container(object):
    frames = []
    
    def __init__(self):
        print("dans container")
        pass
        
    def openPipe(self):
        command = ["ffmpeg",
                   "-y", #overwrite la video precedente
                   "-f", "rawvideo",
                   "-vcodec", "rawvideo",
                   "-s", "1280x720",
                   "-pix_fmt", "rgb24",
                   "-r", "60",
                   "-i", "-", #on passe la donnee par la pipe
                   "-an",
                   '-vcodec', 'libx264',
                   '-pix_fmt', 'yuv420p',
                   "/home/paul/psVidTex/test.mp4"
        ]

        self.pipe = sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)

        print("FFMPEG's pipe opened, ", os.getcwd())

    def addFrameToMovie(self, frame):
        print(frame.tostring()[:100])
        self.pipe.stdin.write(frame.tostring())
        self.pipe.stdin.flush()
        print("Frame written")

    def closePipe(self):
        self.pipe.stdin.close()
        self.pipe.wait()
        
    def convertToUInt8Frame(self, frame):
        return np.array(frame, dtype="uint8")

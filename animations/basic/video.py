#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

import os
import re
import io
import cv2
import numpy as np
from subprocess import *
from PIL import Image

from animations.animation import Animation
from constants.constants import *

class Video(Animation):
    def __init__(self, video_path, timestamp):
        super().__init__()
        self.timestamp = timestamp
        self.raw_video_path = os.path.join(os.path.expanduser('~'), "psVidTex/" + video_path)
        self.current_dir = os.getcwd()
        self.video_info = self.get_video_info()
        self.change_video_according_to_movie()
        self.cap = cv2.VideoCapture(self.video_path)
        self.half_video = False
        self.focus_on_head = False
        self.head_classifier = cv2.CascadeClassifier("/home/paul/psVidTex/constants/haar.xml")


    def change_video_frame_rate(self, frame_rate):
        new_filename = os.path.splitext(self.raw_video_path)[0] + "_new_fr.mp4"
        if not os.path.exists(new_filename):
            print("here")
            cmd = "ffmpeg -y -i %s -filter:v fps=%i %s" % (self.raw_video_path, frame_rate, new_filename)
            cmd = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
            out, err = cmd.communicate()
            if cmd.returncode != 0:
                print("Error in FFMPEG changing frame_rate : " + out)
        return new_filename

    def get_video_frame(self, frame):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.timestamp[0] + frame)
        ret, frame = self.cap.read()
        color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return color_frame

    def get_video_frame_hacky(self, frame):
        tmpFile = self.current_dir + "/frame_tmp_file.png"
        command = "ffmpeg -y -i %s -vf \"select=eq(n\,%i)\" -vframes 1 %s" % (self.video_path, frame, tmpFile)
        cmd = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
        out, err = cmd.communicate()
        if cmd.returncode != 0:     
            print("Error in FFMPEG changing frame_rate : " + out)
        print(command)
        print(os.path.exists(tmpFile))
        image_file = open(tmpFile, "rb")
        buffer = image_file.read()
        return np.array(Image.open(io.BytesIO(buffer)))

    def change_video_according_to_movie(self):
        if self.video_info["fps"] != FRAME_RATE:
            self.video_path = self.change_video_frame_rate(FRAME_RATE)
        else:
            self.video_path = self.raw_video_path

    def get_video_info(self):
        metadata = {}
        process = Popen(["ffprobe", "-i", self.raw_video_path], stdout=PIPE, stderr=PIPE)
        _, out = process.communicate()

        fps = r'\d+ fps'
        fps_string = re.findall(fps, str(out))
        if fps_string is not None:
            metadata["fps"] = int(re.findall('\d+', fps_string[0])[0])
        else:
            print("Error, file has no FPS ?!")

        fps = r'[0-9]{4}x\d+'
        fps_string = re.findall(fps, str(out))
        if fps_string is not None:
            tmp = fps_string[0].split('x')
            metadata["width"]  = tmp[0]
            metadata["height"] = tmp[1]
        else:
            print("Error, file has width and height ?!")

        return metadata

    def focus_on_head(self, bool):
        self.focus_on_head = bool

    def search_for_face(self, frame):
        # on convertit l'image en nuance de gris
        data = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # constants ?
        faces = self.head_classifier.detectMultiScale(data, 1.3, 5)
        return faces

    def set_half_video(self, bool, direction=GAUCHE):
        self.half_video = True
        self.half_video_dir = direction

    def render(self, t):
        if self.half_video:
            frame = self.get_video_frame(t)
            size = frame.shape
            if self.half_video_dir == GAUCHE:
                buffer = frame[0:size[0], 0:size[1]//2]
            if self.half_video_dir == DROITE:
                buffer = frame[0:size[0], size[1]//2:size[1]]

            return buffer
        else:
            frame = self.get_video_frame(t)
            # faces_data = self.search_for_face(frame)
            # for (x,y,w,h) in faces_data:
            #     cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
            return frame
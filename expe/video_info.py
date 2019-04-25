#! /usr/bin/env python3
import os
import sys
import re
import tempfile

from subprocess import Popen, PIPE

def getVideoDetails(filepath):
    process = Popen(["ffprobe", "-i", "/home/paul/psVidTex/expe/dummy_video.mp4"], stdout=PIPE, stderr=PIPE)
    _, out = process.communicate()
    fps = r'[0-9]{4}x\d+'
    fps_str = re.findall(fps, str(out))
    print(fps_str[0].split('x'))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./getVideoDetails.py <filepath(absolute or relative)>")
        sys.exit("Syntax Error")
    getVideoDetails(sys.argv[1])

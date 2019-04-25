#! /usr/bin/env python3
import sys
import subprocess
import os

def change_video_frame_rate(filepath, frame_rate):
	new_filename = os.path.splitext(filepath)[0] + "_new_fr.mp4"	
	cmd = "ffmpeg -y -i %s -filter:v fps=%i %s" % (filepath, frame_rate, new_filename)
	cmd = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	out, err = cmd.communicate()
	if cmd.returncode != 0:
		print("Error in FFMPEG changing frame_rate : " + out)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Syntax Error")
    change_video_frame_rate(sys.argv[1], 10)
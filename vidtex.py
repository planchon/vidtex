#! /usr/bin/python3
#coding: utf8

import argparse
import importlib
import os
import inspect
import traceback

from movie.movie import Movie

def getConfiguration():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file", help="path to the file to render (the python one)"
    )
    args = parser.parse_args()
    config = {
        "file": args.file,
        "video-quality": (1280,720),
        "framerate": 60,
        "renderName": "testRender.mp4"
    }

    return config

def getFileToRender(fileToRender):
    try:
        return importlib.import_module(fileToRender.replace(".py", "").replace(os.sep, "."))
    except Exception:
        print("----- ERROR : MAIN_IMPORT_MODULE ----- \n")
        traceback.print_exc()
        print("----- ERROR : MAIN_IMPORT_MODULE -----")


def isScene(obj):
    if not inspect.isclass(obj):
        return False
    if not issubclass(obj, Movie):
        return False
    if obj == Movie:
        return False
    return True

def getMovieInFile(name, conf):
    if len(name) == 0:
        print("pas de movie")
        return []
    if len(name) > 0:
        return list(name.values())
    return []

def main():
    config = getConfiguration()
    if config["file"][-1] == '/':
        fileToRender = getFileToRender(config["file"] + "movie_main.py")
    else:
        fileToRender = getFileToRender(config["file"] + "/movie_main.py")

    movieName = dict(inspect.getmembers(fileToRender, isScene))

    movieClass = getMovieInFile(movieName, config)
    
    for movie in movieClass:
        try:
            movie()
        except Exception:
            print("----- ERROR : MAIN ----- \n")
            traceback.print_exc()
            print("----- ERROR : MAIN -----")
            
if __name__ == "__main__":
    main()

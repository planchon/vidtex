#! /usr/bin/python3
#coding: utf8


import argparse
import importlib
import os
import inspect
import traceback

from scene.Scene import Scene

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
    return importlib.import_module(fileToRender.replace(".py", "").replace(os.sep, "."))

def isScene(obj):
    if not inspect.isclass(obj):
        return False
    if not issubclass(obj, Scene):
        return False
    if obj == Scene:
        return False
    return True

def getSceneInFile(name, conf):
    if len(name) == 0:
        print("pas de scene")
        return []
    if len(name) > 0:
        return list(name.values())
    return []

def render(scene):
    pass

def main():
    config = getConfiguration()
    fileToRender = getFileToRender(config["file"])

    sceneName = dict(inspect.getmembers(fileToRender, isScene))

    for SceneClass in getSceneInFile(sceneName, config):
        try:
            # la en gros on appelle la scene, donc on appelle sa fonction
            # play et donc on fait le rendu.
            render(SceneClass())
        except:
            # la on a eu une erreur (wtf deja) et ensuite on la trace            
            print("\n\nERROR :\n")
            traceback.print_exc()
            print("END ERROR.\n\n")
            
if __name__ == "__main__":
    main()

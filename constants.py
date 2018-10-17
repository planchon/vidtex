import os

USER_TO_RENDER = "PAUL"

if USER_TO_RENDER == "PAUL":
    LATEX_RENDER_DIR = os.path.join(os.path.expanduser('~'), "psVidTex/.out/tex")
    VIDEO_RENDER_DIR = os.path.join(os.path.expanduser('~'), "psVidTex/.out/vid")
    IMAGE_RENDER_DIR = os.path.join(os.path.expanduser('~'), "psVidTex/.out/img")
else:
    LATEX_RENDER_DIR = "A DEFINIR"
    VIDEO_RENDER_DIR = "A DEFINIR" 
    IMAGE_RENDER_DIR = "A DEFINIR"

LATEX_TEMPLATE_FILE = "latex/template.tex"
LATEX_TEXT_TO_REMPLACE = "textHere"

import sys, os
from subprocess import call
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

import hashlib
from constants import *

class TexGenerator(object):
    texRender   = ""
    texFileName = ""
    
    def generateUniqueID(self):
        return hashlib.sha256(self.texRender).hexdigest(x)

    def div_to_svg(texFile):
        result = texFile.replace(".div", ".svg")
        if not os.path.exists(result):
            command = ["dvisvgm", texFile, "-n", "-v", "0", "-o", result]
            os.system(" ".join(command))
        return result

    def generateTexFile(expression):
        result = os.path.join(LATEX_RENDER_DIR, self.texFileName + ".tex")
        if not os.exists(result):
            print("Creation de \"%s\" a %s" % (expression, result))
            with open(LATEX_TEMPLATE_FILE, "r") as latex:
                body = latex.read().replace("\n", "")

            body = body.replace(LATEX_TEXT_TO_REMPLACE, expression

            with open(result, "w") as outfile:
                outfile.write(body)
                                
        return result
    
    def tex_to_dvi(self):
        result = os.path.join(LATEX_RENDER_DIR, self.texFileName + ".tex")
        if not os.path.exists(result):
            command = ["latex", "-interaction=batchmode", "-halt-on-error", "-output-directory=" + LATEX_RENDER_DIR, texFileName]
            exitCode = os.system(" ".join(command))

            if exitCode != 0:
                log_file = self.texFileName + ".log"
                raise Exception("Latex a eu une erreur. Le log se trouve dans %s" % log_file)

        return result

    def __init__(self, expression):
        pass

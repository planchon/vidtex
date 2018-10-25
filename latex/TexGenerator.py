import sys, os
from subprocess import call
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

import hashlib
from constants import *

class TexGenerator(object):
    expression  = ""
    fileHased   = ""
    finalFile   = ""
    
    def __init__(self, expression):
        self.expression = expression
        self.fileHased  = self.generateUniqueID(expression)
        
        self.generateTexFile(expression)
        self.tex_to_dvi()
        
        self.finalFile = self.div_to_svg()
        

        
    def generatePath(self, extension):
        return os.path.join(LATEX_RENDER_DIR, self.fileHased + extension)
    
    def generateUniqueID(self, expression):
        return hashlib.sha256(expression.encode("utf-8")).hexdigest()[:16]

    def div_to_svg(self):
        result = self.generatePath(".svg")
        if not os.path.exists(result):
            command = ["dvisvgm", str(self.generatePath(".dvi")), "-n", "-v", "0", "-o", result,  ">", "/dev/null"]
            os.system(" ".join(command))
            
        return result

    def generateTexFile(self, expression):
        result = self.generatePath(".tex")
        if not os.path.exists(result):
            print("Creation de \"%s\" a %s" % (expression, result))
            with open(LATEX_TEMPLATE_FILE, "r") as latex:
                body = latex.read()

            body = body.replace(LATEX_TEXT_TO_REMPLACE, expression)

            with open(str(self.generatePath(".tex")), "w") as outfile:
                outfile.write(body)
    
    def tex_to_dvi(self):
        result = self.generatePath(".div")
        if not os.path.exists(result):
            command = ["latex", "-interaction=batchmode", "-output-directory=" + LATEX_RENDER_DIR, str(self.generatePath(".tex")), ">", "/dev/null"]
            exitCode = os.system(" ".join(command))


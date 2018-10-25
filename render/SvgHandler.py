from xml.dom import minidom

class SVGHandler():

    def __init__(self, svgFile):
        svgData = self.openDocument(svgFile)
        defs    = self._getDefs(svgData)
        ids     = self._getIDs(svgData)
        
    def openDocument(self, path):
        return minidom.parse(path)

    def _getDefs(self, svgData):
        return svgData.getElementsByTagName('path')

    def _getIDs(self, svgData):
        return svgData.getElementsByTagName('use')

    def getDefs(self):
        return self.defs

    def getIDs(self):
        return self.ids
    

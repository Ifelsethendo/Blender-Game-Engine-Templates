import bpy
import glob
import bge
import os

## get a list of all the fonts installed on Windows modify for your OS or font directory
fontList = glob.glob("C:\\Windows\\Fonts\\*.ttf")

## define this scripted text object to the game engine
scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
TextObject = cont.owner
TextObject['length'] = len(fontList)
TextObject['init'] = True

## choose font by current value of scripted objects count property
def cycleFonts():
        if hasattr(TextObject.blenderObject.data, 'font' ) is True:
            fontName = os.path.basename(fontList[TextObject['count']])
            TextObject['Font'] =  fontName
            ## if the font is unsupported then report with error      
            try:
                newFont = bpy.data.fonts.load(fontList[TextObject['count']])
                TextObject['Text'] =  os.path.basename(fontList[TextObject['count']])
                TextObject.blenderObject.data.font = newFont
            except:
                TextObject['Text'] =  "error:\n" + fontName
                TextObject['Font'] =  "error:" + fontName
                
                  
            

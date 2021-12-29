import bpy
import bge
import os

# get current directory
blendFilePath = bpy.data.filepath
directory = os.path.dirname(blendFilePath)

global count
lines = []
    
filePath = directory +'\\test.txt'
print(filePath)
with open(filePath) as f:
    lines = f.readlines()  


## define this scripted text object
scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
TextObject = cont.owner
TextObject['length'] = len(lines)
TextObject['init'] = True

def displayLines():
    count = TextObject['line']
    count += 1
    print(count)
    
    if count > len(lines):
        TextObject['end'] = True
        return

    TextObject['Text'] = lines[count]
    TextObject['line'] = count
    
    ## RENDER TO PNGS IF YOU WANT TO
    #number = str('%04d' % TextObject['line'])
    #bge.render.makeScreenshot('//frame' + number + '.png')
    
    



     
    
    
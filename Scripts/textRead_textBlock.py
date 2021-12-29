import bpy
import bge

''' READS TEXT BLOCK STORED IN BLEND FILE '''

global count
lines = []
    
packedText = bpy.data.texts['test.txt']
textString = packedText.as_string()
lines = textString.splitlines()


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
    
    



     
    
    
import bpy
import bge
## expand and contracts an object, in this case an explosion

def expand():
    ## define this scripted  object
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    thisObject = cont.owner
    scale = thisObject['scale'] + 0.07
    thisObject.scaling = [scale,scale,scale]
    thisObject['scale'] = scale
    
   

def collapse():  
    ## define this scripted  object
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    thisObject = cont.owner  
    scale = thisObject['scale'] - 0.02
    thisObject.scaling = [scale,scale,scale]
    thisObject['scale'] = scale
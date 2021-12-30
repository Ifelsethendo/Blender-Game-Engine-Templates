import bpy
import bge

## define this scripted  object
scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
thisObject = cont.owner

''' reset the name based on the current 
    target property copied from the crosshair
    so that the missile can seek it     '''
    
targetName = "Target" + str(thisObject['target'])
thisObject.name = targetName
thisObject['targetName'] = targetName


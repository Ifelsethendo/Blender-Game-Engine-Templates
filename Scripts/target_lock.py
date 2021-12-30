import bpy
import bge

## define this scripted  object
scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
thisObject = cont.owner

''' target property is copied from the crosshair
    the target object renames itself based on the property
    the missile locks onto the object with that name   '''

targetName = "Target" + str(thisObject['target'])
thisObject['targetName'] = targetName

print(scene.objects)
target = scene.objects[targetName]

thisObject.actuators['Steering'].target = target
thisObject['step'] = 2



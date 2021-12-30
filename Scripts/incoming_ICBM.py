import bpy
import bge

## define this scripted  object
scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
thisObject = cont.owner

## choose a city to target based on random integer property
targetName = "City" + str(thisObject['RND'])
thisObject['targetName'] = targetName

target = scene.objects[targetName]

thisObject.actuators['Steering'].target = target
thisObject['step'] = 2
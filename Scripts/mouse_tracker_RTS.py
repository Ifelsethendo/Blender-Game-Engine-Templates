import bpy
import bge

####
## MOUSE TRACKER
## FROM https://youtu.be/-IeNnw6zzvQ
## CLICK AND DRAG TO MOVE TRACKER
#m ouse is tracked by ScriptedTracker object during mouse move
# GoRing will be placed at the clicked location
# RTSUnit will travel to the GoRing

####

def main():

    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()

    mouse_over = cont.sensors["mouse_over"]
    mouse_click = cont.sensors["mouse_leftclick"]

    if mouse_over.positive:
        tracker = scene.objects["ScriptedTracker"]
        tracker.worldPosition = mouse_over.hitPosition
        tracker.worldPosition.z += 1

    if mouse_over.positive and mouse_click.positive:
        target = scene.objects["GoRing"]
        target.worldPosition = mouse_over.hitPosition
        target.worldPosition.z = 0
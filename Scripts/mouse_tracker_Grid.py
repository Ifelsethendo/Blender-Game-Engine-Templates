
import bge
####
## MOUSE TRACKER  GRID UNITS
## FROM https://youtu.be/-IeNnw6zzvQ
## CLICK AND DRAG TO MOVE TRACKER
## Tracker moves only to grid location of FPSUnit plane
## Click drops cubes at mouse location
####

def main():
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    own = cont.owner

    mouse_over = cont.sensors["mouse_over"]
    #mouse_click = cont.sensors["mouse_leftclick"]

    if mouse_over.positive:
        tracker = scene.objects["ScriptedTracker"]
        tracker.worldPosition =  own.worldPosition
        tracker.worldPosition.z += .1


import bge

####
## MOUSE TRACKER
## FROM https://youtu.be/-IeNnw6zzvQ
## CLICK AND DRAG TO MOVE TRACKER
####

def main():
    loc = [0,0,0]
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()

    mouse_over = cont.sensors["mouse_over"]
    mouse_click = cont.sensors["mouse_leftclick"]

    if mouse_over.positive and mouse_click.positive:
        tracker = scene.objects["Tracker"]
        xyz = mouse_over.hitPosition
        tracker.worldPosition = xyz 
        
        



        

import bge

####
## MOUSE TRACKER
## FROM https://youtu.be/-IeNnw6zzvQ
## TRACK MOVES THE CROSSHAIR INTO MOUSE POSITION
####

def main():
    loc = [0,0,0]
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()

    mouse_over = cont.sensors["mouse_over"]
   # mouse_click = cont.sensors["mouse_leftclick"]

    if mouse_over.positive:
        tracker = scene.objects["Crosshair"]
        xyz = mouse_over.hitPosition
        xyz.y = 0
        tracker.worldPosition = xyz 
        
        



        
import bge

####
## MOUSE paddle
## FROM https://youtu.be/-IeNnw6zzvQ
## CLICK AND DRAG TO MOVE paddle
####

def main():
    loc = [0,0,0]
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()

    mouse_over = cont.sensors["mouse_over"]
    #mouse_click = cont.sensors["mouse_leftclick"]
    #and mouse_click.positive
    if mouse_over.positive:
        paddle = scene.objects["Paddle"]
        xyz = mouse_over.hitPosition
        xyz.y = -40
        zyz.z = 0p
        paddle.worldPosition = xyz

        
        
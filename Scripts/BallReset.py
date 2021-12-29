import bge


## Reset the ball if it hits the bottom wall
loc = [0,-4,0]
scene = bge.logic.getCurrentScene()
#cont = bge.logic.getCurrentController()
ball = scene.objects["Sphere"]
ball.worldPosition = loc
    
 
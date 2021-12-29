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
    own = cont.owner
    m = bge.logic.mouse.position
    
     ## checking values of mouse/paddle screen activity
    
    own['mx'] = m[0]
    own['my'] = m[1]
    mx = m[0]
       
   ## if mouse X > .95 or < .095 freeze the mouse there
    if m[0] < 0.095:
       mx = 0.1
    if m[0] > 0.95:
       mx = 0.94
    # keep mouse in screen
    bge.logic.mouse.position = (mx, 0.5)   
    
    mouse_over = cont.sensors["mouse_over"]
    xyz = mouse_over.hitPosition
    own['x'] = xyz.x
    own['y'] = xyz.y
    own['z'] = xyz.z

    if mouse_over.positive:
        paddle = scene.objects["Paddle"]
        
        xyz.y = -40
        xyz.z = 0
        
        # set the position of the paddle
        paddle.worldPosition = xyz

        
        
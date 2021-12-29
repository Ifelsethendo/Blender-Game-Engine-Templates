import bge
## Make sure the ball doesn't get stuck in a horizontal loop

def check_vel():
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    own = cont.owner
    velchk = own['VelY']
    play = own['Play']
    
    ball = scene.objects["Sphere"]
    loc = ball.worldPosition 
    if loc.z != 0:
        loc.z = 0
        ball.worldPosition = loc
        
    linearVel = ball.localLinearVelocity 
    
    own['VelY'] = linearVel.y
    # if the absolute vertical velocity less than or equal 30, push it to 40 (up)
    if abs(linearVel.y) <= 30 and play == True:           
        linearVel.y = 40
        ball.localLinearVelocity = linearVel
        

             
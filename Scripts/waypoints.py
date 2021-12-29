import bge

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
own  = cont.owner


curWaypoint = own['Waypoint']
seek = own.actuators['TargetWaypoint'] 

## detect collision with waypoint set next waypoint
hitObj = own.sensors['Waypoint'].hitObject

if hitObj is not None:
   ## convert number name to integer
    hitNum = int(hitObj.name) 
    hitNum += 1
    own['Waypoint'] = hitNum
    #convert integer back to string
    targetName = str(hitNum)

if own['Waypoint'] > 34:
    own['Waypoint'] = 1
  
## set controller owner seek actuator target to waypoint    
targetName =  str(own['Waypoint'])
varTarget =  scene.objects[targetName]
seek.target = str(varTarget)

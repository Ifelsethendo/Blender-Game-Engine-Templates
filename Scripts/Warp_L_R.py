import bge

## Warp the player from one side of map to next at exits

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()

leftWarp = scene.objects["LeftWarpIn"]
leftLoc = leftWarp.worldPosition

rightWarp = scene.objects["RightWarpIn"]
rightLoc = rightWarp.worldPosition

player = scene.objects["Player"]


def warpLeft():
    # set the position of the player
    player.worldPosition = leftLoc

def warpRight():
    # set the position of the player
    player.worldPosition = rightLoc

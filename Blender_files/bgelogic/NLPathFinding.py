# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    PAR0000 = nodes.ActionFindObject()
    PAR0001 = nodes.ParameterObjectAttribute()
    ACT0002 = nodes.ActionNavigateWithNavmesh()
    ACT0003 = nodes.ActionInstalSubNetwork()
    CON0004 = nodes.OnNextFrame()
    PAR0000.game_object = "NLO:Player"
    PAR0001.game_object = PAR0000
    PAR0001.attribute_name = "worldPosition"
    ACT0002.condition = CON0004
    ACT0002.moving_object = "NLO:Enemy"
    ACT0002.rotating_object = "NLO:Enemy"
    ACT0002.navmesh_object = None
    ACT0002.destination_point = PAR0001
    ACT0002.move_dynamic = True
    ACT0002.linear_speed = 1.0299999713897705
    ACT0002.reach_threshold = 1.0
    ACT0002.look_at = True
    ACT0002.rot_axis = 0
    ACT0002.front_axis = 1
    ACT0002.rot_speed = 1.0
    ACT0002.visualize = True
    ACT0003.condition = None
    ACT0003.target_object = "NLO:Enemy"
    ACT0003.tree_name = "PathFinding"
    ACT0003.initial_status = True
    CON0004.input_condition = False
    network.add_cell(PAR0000)
    network.add_cell(ACT0003)
    network.add_cell(PAR0001)
    network.add_cell(CON0004)
    network.add_cell(ACT0002)
    owner["IGNLTree_PathFinding"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__PathFinding')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_PathFinding")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False

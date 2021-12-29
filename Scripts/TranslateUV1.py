import bpy
import bge
from mathutils import Matrix

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
own = cont.owner


## storing UVs here didn't seem to work when retrieving later, but getting height and width did.
def originalUV():
    global uv1
    global uv2
    global uv3
    global uv4
    global height
    global width
    act_obj = bpy.context.window.scene.objects['Sigil'] 
    bpy.context.view_layer.objects.active = act_obj  
    uv1 = act_obj.data.uv_layers.active.data[0].uv
    uv2 = act_obj.data.uv_layers.active.data[1].uv
    uv3 = act_obj.data.uv_layers.active.data[2].uv
    uv4 = act_obj.data.uv_layers.active.data[3].uv
    #print(uv1[1] , uv2[1])
    #print("")
    #print(uv3[1] , uv4[1])
    own['width'] =  (uv3[0]-uv1[0])/2
    own['height']=  (uv3[1]-uv1[1])
    height = own['height']
    width =  own['width']
    
    
def translate(cont):
    #if not cont.sensors[0].positive:
        #return
    c = own['col']
    act_obj = bpy.context.window.scene.objects['Sigil'] 
    bpy.context.view_layer.objects.active = act_obj  
    uvxya = act_obj.data.uv_layers.active.data[0].uv
    uvxyb = act_obj.data.uv_layers.active.data[1].uv
    uvxyc = act_obj.data.uv_layers.active.data[2].uv
    uvxyd = act_obj.data.uv_layers.active.data[3].uv
    
    if own['col'] <= 9:
     ## add width to current UV coordinates
        uvxya[0] = uvxya[0] + width
        uvxyb[0] = uvxyb[0] + width
        uvxyc[0] = uvxyc[0] + width
        uvxyd[0] = uvxyd[0] + width

    ## if reached end of  texture columns
    if own['col'] > 9:
        own['col'] = 1
        own['row'] += 1
        uvxya[1] = uvxya[1] - height
        uvxyb[1] = uvxyb[1] - height
        uvxyc[1] = uvxyc[1] - height
        uvxyd[1] = uvxyd[1] - height
        uvxya[0] = 0.0
        uvxyb[0] = 0.11100000143051147
        uvxyd[0] = 0.0
        uvxyc[0] = 0.11100000143051147
        print(uvxyd[0])

    ## if reached end of texture rows & columns  reset to top left
    if own['row'] > 8:
        own['col'] = 1
        own['row'] = 1
        uvxya[1] = 0.875437319278717
        uvxyb[1] = 0.875437319278717 
        uvxyc[1] = 1.0 
        uvxyd[1] = 1.0
        uvxya[0] = 0.0
        uvxyb[0] = 0.11100000143051147
        uvxyd[0] = 0.0
        uvxyc[0] = 0.11100000143051147
        
    ## set the UV coordinates    
    act_obj.data.uv_layers.active.data[0].uv = (uvxya)
    act_obj.data.uv_layers.active.data[1].uv = (uvxyb)
    act_obj.data.uv_layers.active.data[2].uv = (uvxyc)
    act_obj.data.uv_layers.active.data[3].uv = (uvxyd)
    own['width']=  uvxya[0]
    own['height']=  uvxya[1]
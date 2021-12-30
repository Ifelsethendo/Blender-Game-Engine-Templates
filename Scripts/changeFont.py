import bpy
import glob
import random

## get a list of all the fonts installed on Windows modify for your OS or font directory
fontList = glob.glob("C:\\Windows\\Fonts\\*.ttf")

selectedObjs = bpy.context.selected_objects

## change the font of all selected Text Objects
## ignoring non text objects
for Obj in selectedObjs:
    if hasattr(Obj.data, 'font' ) is True:
        
        # setting a font by path
        #newFont = bpy.data.fonts.load('C:\\Windows\\Fonts\\calibrib.ttf')
        
        ''' a random font for some variety
            note that its randomized for each object
            use a specified font as above 
            to change all objects to same font     
         '''            
        newFont = bpy.data.fonts.load(random.choice(fontList))
        Obj.data.font = newFont

## choose font by number
def chooseFont_i(number):
    for Obj in selectedObjs:
        if hasattr(Obj.data, 'font' ) is True:
            newFont = bpy.data.fonts.load(fontList[number])
            Obj.data.font = newFont    
            
''' BEWARE OF PACKING FILES AFTER PLAYING WITH RANDOM FONTS
    BLENDER WILL WANT TO PACK ALL THE FONTS INTO THE FILE!!!
'''
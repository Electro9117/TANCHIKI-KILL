# Importing Image class from PIL module
import os
import traceback
from PIL import Image
import numpy as np

lst=[
    (0,4,51,55),(64,4,115,55),(132,0,183,51),(200,0,251,51),(260,0,311,51),(324,0,375,51),(388,0,439,51),(456,0,507,51),
    #(0,60,51,123),(64,60,115,123),(124,64,187,115),(192,64,255,115),(260,60,311,123),(324,60,375,123),(384,64,447,115),(452,64,515,115),
    (0,128,51,187),(64,128,115,187),(124,132,183,183),(192,132,251,183),(260,132,311,191),(324,132,375,191),(388,132,447,183),(456,132,515,183),
    (0,196,55,255),(64,196,119,255),(124,200,183,255),(192,200,251,255),(260,196,315,255),(324,196,379,255),(388,200,447,255),(456,200,515,255),
    #(0,260,51,319),(64,260,115,319),(124,268,183,319),(192,268,251,319),(260,260,311,319),(324,260,375,319),(388,264,447,315),(456,264,515,315),
    (0,324,51,383),(64,324,115,383),(124,332,183,383),(192,332,251,383),(260,328,311,387),(324,328,375,387),(388,328,447,379),(456,328,515,379),
    #(0,392,51,451),(64,392,115,451),(124,400,183,451),(192,400,251,451),(256,392,307,451),(320,392,371,451),(388,396,447,447),(456,396,515,447),
    #(0,456,51,516),(64,456,115,515),(124,460,183,511),(192,460,251,511),(260,456,311,516),(324,456,375,515),(384,460,443,511),(452,460,511,511)
    ]

#directory = ["player1","player2","enemy"]
directory = ["player3","player4"]
level=["lv1","lv2","lv4","lv3"]
movement=["up","left","down","right"]
for i in range(2):
    # Opens a image in RGB mode
    im = Image.open(f"./resources/images/{i+5}.png")

    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size

    # Setting the points for cropped image
    j=1
    lv_update=1
    lv_update1=0
    movement_c=1
    movement_c1=0
    for left,top,right,bottom in lst:

        # Cropped image of above dimension
        # (It will not change original image)
        im1 = im.crop((left, top, right, bottom))
        
        #resize
        newsize = (50, 50)
        im1 = im1.resize(newsize)

        #make image transparent
        im1 = im1.convert("RGBA")
        im1np = np.array(im1)
        white = np.sum(im1np[:,:,:3], axis=2)
        white_mask = np.where(white == 0*3, 1, 0)
        alpha = np.where(white_mask, 0, im1np[:,:,-1])
        im1np[:,:,-1] = alpha 
        im1 = Image.fromarray(np.uint8(im1np))

        #make directory
        try:
            parent_dir = "F:/python/pygame/battle_city/resources/images"
            print(i, lv_update1, movement_c1)
            path = os.path.join(parent_dir, directory[i],level[lv_update1],movement[movement_c1])
            print(path)
            os.makedirs(path)
        except:
            pass

        
        im1.save(f"{path}\{movement_c}.png")
        
        if movement_c==2:
            movement_c=0
            movement_c1+=1

        if lv_update%8==0:
            movement_c1=0
            lv_update1+=1

        j+=1
        lv_update+=1
        movement_c+=1

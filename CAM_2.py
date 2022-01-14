from plateDetection import *
import os
folder = 'Cam 2 Images'
CAM_2_ID = "THIS IS CAM 2"
cam2Data =[]
def recognize_color(R,G,B):
    minimum = 10000
    color_name= ""
    for i in range(len(data)):
        d = abs(R - int(data.loc[i,"R"])) + abs(G- int(data.loc[i,"G"]))+ abs(B- int(data.loc[i,"B"]))
        if  (d <= minimum):
            minimum = d
            color_name = data.loc[i, "color_name"]
    return(color_name)
def cam2List():
    for path in os.listdir(folder):
        full_path = os.path.join(folder, path)
        if os.path.isfile(full_path):
            cam2Data.append(Detection(full_path))
    return cam2Data

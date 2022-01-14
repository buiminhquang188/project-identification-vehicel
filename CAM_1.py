from plateDetection import *
import os
folder = 'Cam 1 Images'
CAM_1_ID = "THIS IS CAM 1"
cam1Data =[]
def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(data)):
        d = abs(R - int(data.loc[i,"R"])) + abs(G- int(data.loc[i,"G"]))+ abs(B- int(data.loc[i,"B"]))
        if  (d <= minimum):
            minimum = d
            cname = data.loc[i, "color_name"]
    return(cname)
def cam1List():
    for path in os.listdir(folder):
        full_path = os.path.join(folder, path)
        if os.path.isfile(full_path):
            cam1Data.append(Detection(full_path))
    return cam1Data

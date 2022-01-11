import cv2
import numpy as np
import pandas as pd
 
img = cv2.imread("C:\\Users\\thang\\Desktop\\project-identification-vehicel\\License-Plate-Recognition-main\\car_img.png")
index = ["color", "color_name", "hex", "R", "G", "B"]
data = pd.read_csv("C:\\Users\\thang\\Desktop\\project-identification-vehicel\\License-Plate-Recognition-main\\colors.csv", names=index, header=None)
clicked = False
r = g = b = xpos = ypos = 0

def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(data)):
        d = abs(R- int(data.loc[i,"R"])) + abs(G- int(data.loc[i,"G"]))+ abs(B- int(data.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = data.loc[i,"color_name"]
    return cname
def get_R_G_B():
    global b,g,r,xpos,ypos, clicked
    b,g,r = img[xpos,ypos]
    b = int(b)
    g = int(g)
    r = int(r)
# cv2.namedWindow('Color Recognition App')
# cv2.setMouseCallback('Color Recognition App', mouse_click)
# while(1):
#     cv2.imshow("Color Recognition App",img)
#     if (clicked):

#         #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
#         cv2.rectangle(img,(20,20), (750,60), (b,g,r), 2)
# #Creating text string to display( Color name and RGB values )
#         text = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
#         print(text)
#         #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
#         cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
# #For very light colours we will display text in black colour
#         if(r+g+b>=600):
#             cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
#         clicked=False
#     if cv2.waitKey(20) & 0xFF ==27:
#         break
# cv2.destroyAllWindows()

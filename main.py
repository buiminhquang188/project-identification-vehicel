from CAM_1 import *
from CAM_2 import *
from IDGenerate import *
from plateDetection import *
import mysql.connector
ID = []
if Detection("Main Images/1.jpg") in  cam1List():
    ID = idGenerate((cam1List()[1])[0], (cam1List()[1])[1], CAM_1_ID)
    print(ID)
elif  Detection("Main Images/1.jpg") in cam2List():
    ID = idGenerate((cam2List()[1])[0], (cam2List()[1])[1], CAM_2_ID)
    print(ID)
else:
    print("Car not here or may be system interupt")
connection = mysql.connector.connect(host='b9llcrzvoxm6pbhe5xxn-mysql.services.clever-cloud.com',
                                     database='b9llcrzvoxm6pbhe5xxn',
                                     user='uijhoo8snd9qskzr',
                                     password='svU4GQlGrl0KVHDf7cLQ')
mycursor = connection.cursor()

query = "INSERT INTO Car (cameraId, twoDigits , color, fourDigits) VALUES (%s, %s, %s, %s)"
val = (str(ID[0]), str(ID[1]), str(ID[2]), str(ID[3]))
mycursor.execute(query, val)

connection.commit()

print(mycursor.rowcount, "record inserted.")
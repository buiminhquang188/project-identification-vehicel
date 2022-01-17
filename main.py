from CAM_1 import *
from CAM_2 import *
from IDGenerate import *
from plateDetection import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import mysql.connector
from datetime import datetime
from PyQt5.QtGui import QIcon, QPixmap

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
folder = "Main Images"
class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("Resource/mainWindow.ui", self)
        self.startBut = self.findChild(QtWidgets.QPushButton, 'startButton')
        self.path = self.findChild(QtWidgets.QComboBox, 'comboBox')
        self.log = self.findChild(QtWidgets.QListWidget, 'listWidget')
        self.CarIMG = self.findChild(QtWidgets.QLabel, 'carImages')
        self.CamIMG = self.findChild(QtWidgets.QLabel, 'camImages')
        self.startBut.clicked.connect(self.startFunc)
        for path in os.listdir(folder):
            full_path = os.path.join(folder, path)
            if os.path.isfile(full_path):
                self.path.addItem(full_path)
        self.show()
    def startFunc(self):
        if Detection(self.path.currentText()) in cam1List():
            ID = []
            ID = idGenerate(Detection(self.path.currentText())[0], (Detection(self.path.currentText()))[1], CAM_1_ID)
            self.log.addItem(f'Current Time : {current_time}    Camera Name: {CAM_1_ID}  Infor : {str(ID[1]), str(ID[2]),str(ID[3])}')
            self.IMGShow()
        elif Detection(self.path.currentText()) in cam2List():            
            ID = []
            ID = idGenerate(Detection(self.path.currentText())[0], (Detection(self.path.currentText()))[1], CAM_2_ID)
            self.log.addItem(f'Current Time : {current_time}    Camera Name: {CAM_2_ID} Infor : {str(ID[1]), str(ID[2]),str(ID[3])} ')
            self.IMGShow()  
        else:
            ID = []
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText("Car not here or may be system interupt")
            msg.setWindowTitle("Alert")
            msg.exec_()
            self.log.addItem("Car not here or may be system interupt")
        connection = mysql.connector.connect(host='b9llcrzvoxm6pbhe5xxn-mysql.services.clever-cloud.com',
                                             database='b9llcrzvoxm6pbhe5xxn',
                                             user='uijhoo8snd9qskzr',
                                             password='svU4GQlGrl0KVHDf7cLQ')
        myCursor = connection.cursor()
        query = "INSERT INTO Car (cameraId, twoDigits , color, fourDigits) VALUES (%s, %s, %s, %s)"
        val = (str(ID[0]), str(ID[1]), str(ID[2]), str(ID[3]))
        myCursor.execute(query, val)
        connection.commit()
        self.log.addItem(f'{myCursor.rowcount} record inserted.')
    def IMGShow(self):
        Campixmap = QPixmap(self.path.currentText())
        self.CamIMG.setGeometry(0,310,380,200)
        self.CamIMG.setPixmap(Campixmap)
        self.CamIMG.resize(380,480)
        Carpixmap = QPixmap('Cropped Images-Text/Croped.png')
        self.CarIMG.setGeometry(380,310,380,200)
        self.CarIMG.setPixmap(Carpixmap)
        self.CarIMG.resize(380,480)
app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec_()
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap
import sys
import mysql.connector
from datetime import datetime
import os
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
        for path in os.listdir(folder):
            full_path = os.path.join(folder, path)
            if os.path.isfile(full_path):
                self.path.addItem(full_path)
        
        Campixmap = QPixmap("Main Images/2.jpg")
        self.CamIMG.setGeometry(0,310,380,200)
        self.CamIMG.setPixmap(Campixmap)
        self.CamIMG.resize(380,480)
        Carpixmap = QPixmap('Cropped Images-Text/Croped.png')
        self.CarIMG.setGeometry(380,310,380,200)
        self.CarIMG.setPixmap(Carpixmap)
        self.CarIMG.resize(380,480)
        
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec_()
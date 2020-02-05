from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import mysql.connector

class Profiles_Win(QDialog):
    def __init__(self, *args, **kwargs):
        super(Profiles_Win, self).__init__(*args, **kwargs)
        self.ui = uic.loadUi('UI Files/DeviceProfilesUI.ui', self)  

        #Button method calls are commented until methods are completed

        #Reset Button Setup
        self.p1ResetButton = self.findChild(QtWidgets.QPushButton, 'P1ResetButton')
        #self.p1ResetButton.clicked.connect(self.resetConfigTable,1) 
        self.p2ResetButton = self.findChild(QtWidgets.QPushButton, 'P2ResetButton')
        #self.p2ResetButton.clicked.connect(self.resetConfigTable,2)
        self.p3ResetButton = self.findChild(QtWidgets.QPushButton, 'P3ResetButton')
        #self.p3ResetButton.clicked.connect(self.resetConfigTable,3)
        self.p4ResetButton = self.findChild(QtWidgets.QPushButton, 'P4ResetButton')
        #self.p4ResetButton.clicked.connect(self.resetConfigTable,4)
        self.p5ResetButton = self.findChild(QtWidgets.QPushButton, 'P5ResetButton')
        #self.p5ResetButton.clicked.connect(self.resetConfigTable,5)

        #Save Button Setup
        self.saveConfigsButton = self.findChild(QtWidgets.QPushButton, 'SaveProfilesButton')
        #self.saveConfigsButton.clicked.connect(self.saveConfigs)

        #Cancel Button Setup
        self.cancelProfilesButton = self.findChild(QtWidgets.QPushButton, 'CancelProfilesButton')
        self.cancelProfilesButton.clicked.connect(self.close) 

    #def resetConfigTable(self, configNum):
        #Deletes all entries in specified device config table
        

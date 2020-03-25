from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import mysql.connector

#Database Credentials
dbConnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="powermonitor"
)

class Profiles_Win(QDialog):
    def __init__(self, *args, **kwargs):
        super(Profiles_Win, self).__init__(*args, **kwargs)
        self.ui = uic.loadUi('UI Files/DeviceProfilesUI.ui', self)  

        #Text Entry Setup
        self.p1Text = self.findChild(QtWidgets.QLineEdit, 'P1TitleEntry')
        self.p2Text = self.findChild(QtWidgets.QLineEdit, 'P2TitleEntry')
        self.p3Text = self.findChild(QtWidgets.QLineEdit, 'P3TitleEntry')
        self.p4Text = self.findChild(QtWidgets.QLineEdit, 'P4TitleEntry')
        self.p5Text = self.findChild(QtWidgets.QLineEdit, 'P5TitleEntry')

        #Reset Button Setup
        self.p1ResetButton = self.findChild(QtWidgets.QPushButton, 'P1ResetButton')
        self.p1ResetButton.clicked.connect(self.resetConfig,1) 
        self.p2ResetButton = self.findChild(QtWidgets.QPushButton, 'P2ResetButton')
        self.p2ResetButton.clicked.connect(self.resetConfig,2)
        self.p3ResetButton = self.findChild(QtWidgets.QPushButton, 'P3ResetButton')
        self.p3ResetButton.clicked.connect(self.resetConfig,3)
        self.p4ResetButton = self.findChild(QtWidgets.QPushButton, 'P4ResetButton')
        self.p4ResetButton.clicked.connect(self.resetConfig,4)
        self.p5ResetButton = self.findChild(QtWidgets.QPushButton, 'P5ResetButton')
        self.p5ResetButton.clicked.connect(self.resetConfig,5)

        #Save Button Setup
        self.saveConfigsButton = self.findChild(QtWidgets.QPushButton, 'SaveProfilesButton')
        self.saveConfigsButton.clicked.connect(self.saveConfigChanges)
        

        #Cancel Button Setup
        self.cancelProfilesButton = self.findChild(QtWidgets.QPushButton, 'CancelProfilesButton')
        self.cancelProfilesButton.clicked.connect(self.close) 

        #Load Profile Data
        currentProfiles = self.getConfigData()
        self.p1Text.insert(currentProfiles[0][0])
        self.p2Text.insert(currentProfiles[1][0])
        self.p3Text.insert(currentProfiles[2][0])
        self.p4Text.insert(currentProfiles[3][0])
        self.p5Text.insert(currentProfiles[4][0])

    def getConfigData(self):
        #Loads saved configs to UI
        sql = 'SELECT PROFILES_NAME FROM profiles'
        cursor = dbConnection.cursor()
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult

    def resetConfig(self, configNum):
        #Resets config to default value
        sql = 'UPDATE profiles SET PROFILES_NAME = %s, PROFILES_DESCRIPTION = %s WHERE PROFILES_ID = %s'
        vals = ['Default ' + configNum, 'Default profile ' + configNum, configNum]
        cursor = dbConnection.cursor()
        cursor.execute(sql, vals)
        dbConnection.commit()
        cursor.close()  

    def saveConfigChanges(self):
        #This is horrendous, please come up with a better solution to update all 5 rows
        self.updateConfigTable('1', self.p1Text.text())
        self.updateConfigTable('2', self.p2Text.text())
        self.updateConfigTable('3', self.p3Text.text())
        self.updateConfigTable('4', self.p4Text.text())
        self.updateConfigTable('5', self.p5Text.text())
        self.close()    #Closes the window when settings are saved

    def updateConfigTable(self, idVal, nameVal):
        #Updates config values
        sql = 'UPDATE profiles SET PROFILES_NAME = %s WHERE PROFILES_ID = %s'  #Update this later if we decide to use the descriptions
        vals = [nameVal, idVal]
        cursor = dbConnection.cursor()
        cursor.execute(sql, vals)
        dbConnection.commit()
        cursor.close()  

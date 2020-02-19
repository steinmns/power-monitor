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

class Settings_Win(QDialog):
    def __init__(self, *args, **kwargs):
        super(Settings_Win, self).__init__(*args, **kwargs)
        self.ui = uic.loadUi('UI Files/SettingsMenuUI.ui', self)  

        #Save Button Setup
        self.saveSettingsButton = self.findChild(QtWidgets.QPushButton, 'SaveSettingsButton')
        self.saveSettingsButton.clicked.connect(self.updateSettings)   
        
        #Cancel Button Setup
        self.cancelSettingsButton = self.findChild(QtWidgets.QPushButton, 'CancelSettingsButton')
        self.cancelSettingsButton.clicked.connect(self.close) 

        #Dropdown Setup
        self.appThemeVal = self.findChild(QtWidgets.QComboBox, 'ThemeDropdown')
        self.appProfileVal = self.findChild(QtWidgets.QComboBox, 'ActiveProfileDropdown')
        currentProfiles = self.getAllProfiles()
        activeProfile = self.getActiveSettings()
        it = 0
        for profile in currentProfiles:
            self.appProfileVal.insertItem(it, profile[0])
            it += 1
        self.appProfileVal.setCurrentText(activeProfile[0][1])
        self.appThemeVal.setCurrentText(activeProfile[0][0])

    def getAllProfiles(self):
        #Returns the list of all profiles
        sql = 'SELECT PROFILES_NAME FROM profiles'
        cursor = dbConnection.cursor()
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult

    def getActiveSettings(self):
        #Gets the settings that are currently active
        sql = 'SELECT SETTINGS_THEME, SETTINGS_DEVICE_PROFILE FROM settings WHERE SETTINGS_ID = 1'
        cursor = dbConnection.cursor()
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult

    def updateSettings(self):
        #Saves the changs made to the settings values
        sql = 'UPDATE settings SET SETTINGS_THEME = %s, SETTINGS_DEVICE_PROFILE = %s WHERE SETTINGS_ID = 1'
        vals = [self.appThemeVal.currentText(), self.appProfileVal.currentText()]
        cursor = dbConnection.cursor()
        cursor.execute(sql, vals)
        dbConnection.commit()
        cursor.close()
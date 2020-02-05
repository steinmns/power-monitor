from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import mysql.connector

class Settings_Win(QDialog):
    def __init__(self, *args, **kwargs):
        super(Settings_Win, self).__init__(*args, **kwargs)
        self.ui = uic.loadUi('UI Files/SettingsMenuUI.ui', self)  

        #Save Button Setup
        self.saveSettingsButton = self.findChild(QtWidgets.QPushButton, 'SaveButton')
        #self.saveSettingsButton.clicked.connect(self.updateSettings)   #Commented until the updateSettings method is filled out
        
        #Cancel Button Setup
        self.cancelSettingsButton = self.findChild(QtWidgets.QPushButton, 'CancelSettingsButton')
        self.cancelSettingsButton.clicked.connect(self.close) 

        #self.appThemeVal = self.findChild(QtWidgets.QComboBox, 'ThemeDropdown')
        
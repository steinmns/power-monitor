#PyQT Dependencies
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout

#Graphing Dependencies
import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

#Icon and Styling Dependencies
import qtawesome as qta #Possibly make this only material icons at some point

#Database Dependencies
import mysql.connector

class Main_Win(QMainWindow):
    
    def __init__(self):
        #Constructor Method
        super(Main_Win, self).__init__()
        self.ui = uic.loadUi('UI Files/MainWindowUI.ui', self)   #Loads Main Menu Window

        #Tab Icons
        hometab_icon = qta.icon('mdi.home-outline')
        insighttab_icon = qta.icon('mdi.chart-line')
        self.CentralTabWidget.setTabIcon(0, hometab_icon)
        self.CentralTabWidget.setTabIcon(1, insighttab_icon)

        #Settings Button Setup
        settings_icon = qta.icon('mdi.settings-outline')
        self.SettingsButton = self.findChild(QtWidgets.QPushButton, 'SettingsButton') 
        self.SettingsButton.setIcon(settings_icon)
        #self.SettingsButton.clicked.connect(self.displaySettingsMenu)  #WHEN SETTINGS UI FILES ARE ADDED FINISH THIS

        #Help Button Setup
        help_icon = qta.icon('mdi.help-circle-outline')
        self.HelpButton = self.findChild(QtWidgets.QPushButton, 'HelpButton')
        self.HelpButton.setIcon(help_icon)
        #self.HelpButton.clicked.connect(self.displayHelpWindow)    #WHEN HELP MENU UI FILES ARE ADDED FINISH THIS

    def testGraph(self):
        fig, ax = plt.subplots()
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        counts = [10,3,4,7,2,12,11,7,3,4,1,5]
        ax.plot(months, counts)
        ax.set(xlabel='Month', ylabel='Test Unit', title='Test Plot')
        ax.grid()
        plt.xticks(months, rotation='vertical') #FIX the labels going off the edges

        self.plotWidget = FigureCanvas(fig)
        lay = QtWidgets.QVBoxLayout(self.HomeGraph)  
        lay.setContentsMargins(0, 0, 0, 0)      
        lay.addWidget(self.plotWidget)

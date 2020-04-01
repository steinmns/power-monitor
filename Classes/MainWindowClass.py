#PyQT Dependencies
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout

#External Classes
from Classes.SettingsMenuClass import Settings_Win
from Classes.ProfilesMenuClass import Profiles_Win
from Classes.NotificationsWindowClass import Notifications_Win

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

#Database Credentials
dbConnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="powermonitor"
)

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
        self.SettingsButton.clicked.connect(self.displaySettingsMenu) 

        #Help Button Setup
        help_icon = qta.icon('mdi.help-circle-outline')
        self.HelpButton = self.findChild(QtWidgets.QPushButton, 'HelpButton')
        self.HelpButton.setIcon(help_icon)
        #self.HelpButton.clicked.connect(self.displayHelpWindow)    #WHEN HELP MENU UI FILES ARE ADDED FINISH THIS

        #Profiles Button Setup
        profiles_icon = qta.icon('mdi.account-outline')
        self.ProfilesButton = self.findChild(QtWidgets.QPushButton, 'ProfilesButton')
        self.ProfilesButton.setIcon(profiles_icon)
        self.ProfilesButton.clicked.connect(self.displayProfilesMenu)

        #Notifications Button Setup
        notifications_icon = qta.icon('mdi.alarm-light-outline')
        self.NotificationsButton = self.findChild(QtWidgets.QPushButton, 'NotificationsButton')
        self.NotificationsButton.setIcon(notifications_icon)
        self.NotificationsButton.clicked.connect(self.displayNotificationsWindow)

        #Settings
        appSettings = Settings_Win(self).getActiveSettings()
        self.activeDeviceNum = str((self.getActiveDeviceNum(appSettings[0][1])[0][0]))  #Holds the ID number of the active device profile

        #Load Graph
        self.getProofofConceptGraph()

        #Load Data Table
        self.loadDataTable()

        #Load stats
        self.getAverage(1) #Arg should be changed to actual value when timespan is figured out
        self.getMaxPower(1)
        self.getMinPower(1)

    def getActiveDeviceNum(self, profileName):
        #Gets Device Number of Active Device Profile
        #There is almost certainly a better way to do this
        sql = 'SELECT PROFILES_ID FROM profiles WHERE PROFILES_NAME = %s'
        vals = [profileName]
        cursor = dbConnection.cursor()
        cursor.execute(sql,vals)
        deviceNum = cursor.fetchall()
        cursor.close()
        return deviceNum

    def displaySettingsMenu(self):
        # Displays the Settings Menu when the SettingsButton is pressed
        settingsMenu = Settings_Win(self)
        if settingsMenu.exec_():
            print("Success!")
        else:
            print("Closing Settings Menu")

    def displayProfilesMenu(self):
        #Displays the Profile Configuration Menu when the ProfilesButton is pressed
        profilesMenu = Profiles_Win(self)
        if profilesMenu.exec_():
            print("Success!")
        else:
            print("Closing Profiles Menu")

    def displayNotificationsWindow(self):
        #Displays the Notifications Window when the NotificationsButton is pressed
        notificationsWindow = Notifications_Win(self)
        if notificationsWindow.exec_():
            print("Success!")
        else:
            print("Closing Notifications Menu")

    def getData(self, timespan):
        #Gets power usage data logged over past hour
        #Timespan indicates the scope of the get (hourly/weekly/monthly/yearly)
        sql = 'SELECT FROM WHERE'

    def getAverage(self, timepsan):
        #Gets average power usage over past x time
        #Timespan indicates the scope of the get (hourly/weekly/monthly/yearly)
        sql = 'SELECT AVG(DEVICE' + self.activeDeviceNum + '_VOLTAGE * DEVICE' + self.activeDeviceNum + '_CURRENT) FROM device' + self.activeDeviceNum + '_readings' #Add where clause here that acts on timespan
        cursor = dbConnection.cursor()
        cursor.execute(sql)
        avgPower = cursor.fetchall()
        avgPower = avgPower[0][0]
        cursor.close()
        self.AvgDrawValueLabel.setText('{:.2f}'.format(avgPower))   #Truncates power draw value to 2 decimal places

    def getMaxPower(self, timespan):
        #Gets maximum power usage value over past x time
        sql = 'SELECT MAX(DEVICE' + self.activeDeviceNum + '_VOLTAGE * DEVICE' + self.activeDeviceNum + '_CURRENT) FROM device' + self.activeDeviceNum + '_readings' #Add where clause here that acts on timespan
        cursor = dbConnection.cursor()
        cursor.execute(sql)
        maxPower = cursor.fetchall()
        maxPower = maxPower[0][0]
        self.MaxDrawValueLabel.setText('{:.2f}'.format(maxPower))

    def getMinPower(self, timespan):
        #Gets minimum power usage value over past x time
        sql = 'SELECT MIN(DEVICE' + self.activeDeviceNum + '_VOLTAGE * DEVICE' + self.activeDeviceNum + '_CURRENT) FROM device' + self.activeDeviceNum + '_readings' #Add where clause here that acts on timespan
        cursor = dbConnection.cursor()
        cursor.execute(sql)
        minPower = cursor.fetchall()
        minPower = minPower[0][0]
        self.MinDrawValueLabel.setText('{:.2f}'.format(minPower)) 

    def getLifetimeUsage(self):
        #Gets the total amount of power used by the device
        sql = 'SELECT SUM(COLUMN NAME HERE) FROM WHERE'

    def hourlyGraph(self):
        #Graph of power usage over time for past hour
        #hourly = self.getHourlyData
        
        fig, ax = plt.subplots()
        #ax.plot(minute, power)
        ax.set(xlabel='Month', ylabel='Test Unit', title='Test Plot')
        ax.grid()
        #plt.xticks(months, rotation='vertical') #FIX the labels going off the edges

        self.plotWidget = FigureCanvas(fig)
        lay = QtWidgets.QVBoxLayout(self.HomeGraph)  
        lay.setContentsMargins(0, 0, 0, 0)      
        lay.addWidget(self.plotWidget)

    def getProofofConceptGraph(self):
        #Due to COVID-19, this is the closest we can come to a real graph since we don't have our circuit to collect data
        sql = 'SELECT DEVICE'  + self.activeDeviceNum + '_TIMESTAMP, (DEVICE' + self.activeDeviceNum + '_VOLTAGE*DEVICE'+ self.activeDeviceNum + '_CURRENT) AS DEVICE' + self.activeDeviceNum + '_POWER FROM device' + self.activeDeviceNum + '_readings'
        cursor = dbConnection.cursor()
        cursor.execute(sql)
        powerData = cursor.fetchall()
        cursor.close()
        timeVals = []
        powerVals = []

        for item in powerData:
            timeVals.append(str(item[0].minute) + 'M' + str(item[0].second) +'S')
            powerVals.append(item[1])

        #Graph Setup
        fig, ax = plt.subplots()
        ax.plot(timeVals, powerVals)
        ax.set(xlabel='Time', ylabel='Watts', title='Power Usage vs. Time (Past 10 Minutes)')
        ax.grid()
        plt.xticks(timeVals, rotation='vertical') #FIX the labels going off the edges
        plt.tight_layout()

        self.plotWidget = FigureCanvas(fig)
        lay = QtWidgets.QVBoxLayout(self.HomeGraph)  
        lay.setContentsMargins(0, 0, 0, 0)      #(left, top, right, bottom)
        lay.addWidget(self.plotWidget)

    def loadDataTable(self):
        #Displays all collected data
        sql = 'SELECT DEVICE' + self.activeDeviceNum +'_ID, DEVICE' + self.activeDeviceNum + '_VOLTAGE, DEVICE' + self.activeDeviceNum + '_CURRENT, (DEVICE' + self.activeDeviceNum + '_VOLTAGE*DEVICE' + self.activeDeviceNum + '_CURRENT) AS DEVICE' + self.activeDeviceNum + '_POWER, DEVICE' + self.activeDeviceNum + '_TIMESTAMP FROM device' + self.activeDeviceNum + '_readings'
        cursor = dbConnection.cursor()
        cursor.execute(sql)
        tableData = cursor.fetchall()
        cursor.close()

        header = ["ID","Voltage", "Current", "Power Draw", "DateTime"]
        self.PowerDataTable.setColumnCount(5) #Sets column count to 7
        self.PowerDataTable.setColumnHidden(0, True)  #Hides ID column because it clutters the table in the UI -> used exclusively for edit and delete operations
        self.PowerDataTable.setColumnWidth(1, 75) #Voltage
        self.PowerDataTable.setColumnWidth(2, 75) #Current
        self.PowerDataTable.setColumnWidth(3, 85) #Power Draw
        self.PowerDataTable.setColumnWidth(4, 150) #Datetime
        self.PowerDataTable.setHorizontalHeaderLabels(header) #Sets Column headings
        for row_number, row_data in enumerate(tableData):    #Adds data from select statement to the table
            self.PowerDataTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number != 4:
                    self.PowerDataTable.setItem(row_number, column_number,QtWidgets.QTableWidgetItem('{:.2f}'.format(data)))    #Truncates vals to only 2 decimal places
                else:
                    self.PowerDataTable.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))
        
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

class Notifications_Win(QDialog):
    def __init__(self, *args, **kwargs):
        super(Notifications_Win, self).__init__(*args, **kwargs)
        self.ui = uic.loadUi('UI Files/NotificationsWIndowUI.ui', self)

        #Button Setup
        self.deleteCurrentButton = self.findChild(QtWidgets.QPushButton, 'DeleteCurrentButton')
        self.deleteCurrentButton.clicked.connect(self.deleteSelectedNotification) 

        self.deleteAllButton = self.findChild(QtWidgets.QPushButton, 'DeleteAllButton')
        self.deleteAllButton.clicked.connect(self.deleteAllNotifications) 

        self.closeButton = self.findChild(QtWidgets.QPushButton, 'CloseNotificationsButton')
        self.closeButton.clicked.connect(self.close) 

        #Get Notifications from table
        self.getNotificationMessages()

    def getNotificationMessages(self):
        #Gets all notification messages regardless of whether or not they have been read
        sql = 'SELECT NOTIFICATIONS_ID, NOTIFICATIONS_MESSAGE FROM notifications'
        cursor = dbConnection.cursor()
        cursor.execute(sql)
        notifications = cursor.fetchall()
        cursor.close()

        header = ["ID", "Message"]
        self.NotificationTable.setColumnCount(2) #Sets column count to 7
        self.NotificationTable.setColumnHidden(0, True)  #Hides ID column because it clutters the table in the UI -> used exclusively for edit and delete operations
        self.NotificationTable.setColumnWidth(1, 150)
        self.NotificationTable.setHorizontalHeaderLabels(header) #Sets Column headings
        for row_number, row_data in enumerate(notifications):    #Adds data from select statement to the table
            self.NotificationTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.NotificationTable.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))

    def deleteAllNotifications(self):
        #Deletes all notifications in table 
        sql = "DELETE FROM notifications"
        cursor = dbConnection.cursor()
        cursor.execute(sql)
        dbConnection.commit()
        cursor.close()

    def deleteSelectedNotification(self):
        #Deletes currently selected notification in table
        if(len(self.NotificationTable.selectedItems()) > 0):
            notifID = self.NotificationTable.item(self.NotificationTable.currentRow(), 0).text()
            sql = "DELETE FROM notifications WHERE NOTIFICATIONS_ID = %s"
            vals = [notifID]
            cursor = dbConnection.cursor()
            cursor.execute(sql, vals)
            dbConnection.commit()
            cursor.close()

            #Deleting from MainLogTable
            self.NotificationTable.removeRow(self.NotificationTable.currentRow())
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QIcon
from PyQt4.Qt import QSize, QTableWidgetItem, QColor, QPixmap, QLabel, QSound,\
    QString
from finder import Finder
from entity import Entity
import time
import re
# from mycclock import ClockThread
import threading
import os
from pygame import mixer




class controller:
    
    def __init__(self, ui, window):
        self.ui = ui
        self.window = window
        self.entityes = []
        self.selectedEntity = -1
        self.loadImages()
        self.setIcons()
        self.setEvents()
        self.setTable()
        self.startTime = self.getTime()
        self.elapsTime = None
        self.set_elaps_time(self.getTime() - self.startTime)
        # self.t = threading.Thread(target=self.clockTick, args=(1,self.ui.tableWidget))
        # self.t.daemon = True
        # self.t.start()
        mixer.init()
        mixer.music.load("assets/good2.mp3")
        mixer.music.play()
        
        
        self.t = QtCore.QTimer()
        self.t.timeout.connect(self.clockTick)
        self.t.start(1000)
        pass

    def get_elaps_time(self):
        return self.__elapsTime


    def set_elaps_time(self, value):
        self.__elapsTime = value

    
    def setIcons(self):
        button1 = self.ui.newButton
        icon = QIcon("assets/new.png")
        button1.setIcon(icon)
        button1.setIconSize(QSize(button1.width(), button1.height()))
        
        button2 = self.ui.zvvklButton
        icon = QIcon("assets/zvvkl.png")
        button2.setIcon(icon)
        button2.setIconSize(QSize(button2.width(), button2.height()))
        
        button3 = self.ui.zvotklButton
        icon = QIcon("assets/zvotkl.png")
        button3.setIcon(icon)
        button3.setIconSize(QSize(button3.width(), button3.height()))
        
        pass
    
    def loadImages(self):
        self.picClose = QtGui.QPixmap("assets/close.png")
        self.picGood = QtGui.QPixmap("assets/good.png")
        self.picBad = QtGui.QPixmap("assets/bad.png")
        self.picSetting = QtGui.QPixmap("assets/setting.png")
        pass
    
    def updateEntyties(self):
        for i in self.entityes:
            i.set_time(i.get_time() + 1)
            print "Time " + str(i.get_time()) + " Interval " + str(i.get_interval())
            if i.get_time() > i.get_interval() and i.get_interval() > -1:
                preCondition=i.get_is_found()
                i.set_is_found(i.isFound())
                if i.get_is_found()==False and preCondition==True:
                    mixer.music.play()
                i.set_time(0)
        pass
    
    def updateTable(self, tab):
        tab.clear()
        tab.setRowCount(0)
        for i in self.entityes:
            
            self.addToTable(i.get_is_found(), i.get_header(), tab)
            if i.get_is_found()==False and i.isRing==False:
                
                i.isRing=True
            print "Header !! " + i.get_header()
        pass
    
    def clockTick(self):
        self.updateEntyties()
        self.updateTable(self.ui.tableWidget)
        print "Updated"
        # time.sleep(interval)
        pass
    
    def newButtonClick(self):
        oneElem = Entity("", "", -1)
        self.entityes.append(oneElem)
        # self.addToTable(False, "", self.ui.tableWidget)
        self.updateEntyties()
        self.updateTable(self.ui.tableWidget)
        print "new"
        self.set_elaps_time(self.getTime() - self.startTime)
        print self.get_elaps_time()
        
        
        pass
    
    def zvvklButtonClick(self):
        print "zvvkl"
        pass
    
    def zvotklButtonClick(self):
        print "zvotkl"
        pass
    def saveButtonClick(self):
        # self.addToTable(True, "gg", self.ui.tableWidget)
        '''finder = Finder()
        url = self.ui.lineEdit.text()
        phrase = self.ui.lineEdit_2.text()
        interval = self.ui.lineEdit_3.text()
        
        finder.set_url(url)
        finder.set_phrase(phrase)
        finder.set_interval(interval)
        
        self.addToTable(finder.isFound(), finder.get_phrase(), self.ui.tableWidget)'''
        self.changeEntity(self.selectedEntity)
        self.selectedEntity = -1
        print "save"
        pass
    
    def deleteEntity(self, i):
        del self.entityes[i]
        pass
    
    def showEntity(self, i):
        self.ui.lineEdit.setText(i.get_url())
        self.ui.lineEdit_2.setText(i.get_phrase().decode("utf8"))
        self.ui.lineEdit_3.setText(str(i.get_interval()))
        
        pass
    def changeEntity(self, i):
        if(i != -1):
            url = str(self.ui.lineEdit.text()).encode("utf-8")
            phrase = str(self.ui.lineEdit_2.text())
            interval = int(self.ui.lineEdit_3.text())
            
            self.entityes[i].set_url(url)
            self.entityes[i].set_phrase(phrase)
            self.entityes[i].set_interval(interval)
            
        pass
    
    def clickTable(self, i, j):
        print str(i) + " " + str(j)
        if j == 0:
            self.deleteEntity(i)
            self.updateTable(self.ui.tableWidget)
        elif j == 2:
            self.showEntity(self.entityes[i])
            self.selectedEntity = i
        pass
    
    def setEvents(self):
        self.ui.newButton.clicked.connect(self.newButtonClick)
        self.ui.zvvklButton.clicked.connect(self.zvvklButtonClick)
        self.ui.zvotklButton.clicked.connect(self.zvotklButtonClick)
        self.ui.saveButton.clicked.connect(self.saveButtonClick)
        self.ui.tableWidget.cellClicked.connect(self.clickTable)
        pass
    
    def setTable(self):
        tab = self.ui.tableWidget
        tab.setColumnCount(4)
        tab.setRowCount(0)
        pass
    
    def addToTable(self, isfound, header, tab):
        rowPosition = tab.rowCount()
        tab.insertRow(rowPosition)
        item1 = QTableWidgetItem()
        # item1.setBackground(QtGui.QColor(144, 16, 65))
        lb = QLabel()
        lb.setAlignment(QtCore.Qt.AlignCenter)
        lb.setPixmap(self.picClose)
        
        lb2 = QLabel()
        # lb2.setAlignment(QtCore.Qt.AlignCenter)
       
        lb2.setText(header.decode("cp1251"))
        
        lb3 = QLabel()
        lb3.setAlignment(QtCore.Qt.AlignCenter)
        lb3.setPixmap(self.picSetting)
        
        lb4 = QLabel()
        lb4.setAlignment(QtCore.Qt.AlignCenter)
        if isfound == True :
            lb4.setPixmap(self.picGood)
        else:
            lb4.setPixmap(self.picBad)
            
        
       
        # tab.setItem(0, 0, item1)
        tab.setCellWidget(tab.rowCount() - 1, 0, lb)
        tab.setCellWidget(tab.rowCount() - 1, 1, lb2)
        tab.setCellWidget(tab.rowCount() - 1, 2, lb3)
        tab.setCellWidget(tab.rowCount() - 1, 3, lb4)
        # tab.resizeColumnsToContents()
        tab.setColumnWidth(0, 50)
        tab.setColumnWidth(1, 100)
        tab.setColumnWidth(2, 50)
        tab.setColumnWidth(3, 80)
        tab.setRowHeight(tab.rowCount() - 1, 70)
        pass
    
    def getTime(self):
        t = time.time()
        return t
    
    
    elapsTime = property(get_elaps_time, set_elaps_time, None, None)

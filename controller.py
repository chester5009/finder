from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QIcon
from PyQt4.Qt import QSize, QTableWidgetItem, QColor, QPixmap, QLabel
from finder import Finder
class controller:
    
    def __init__(self, ui, window):
        self.ui = ui
        self.window = window
        self.loadImages()
        self.setIcons()
        self.setEvents()
        self.setTable()
        
        pass
    
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
    
    def newButtonClick(self):
        self.addToTable(True, "gg", self.ui.tableWidget)
        print "new"
        pass
    
    def zvvklButtonClick(self):
        print "zvvkl"
        pass
    
    def zvotklButtonClick(self):
        print "zvotkl"
        pass
    def saveButtonClick(self):
        # self.addToTable(True, "gg", self.ui.tableWidget)
        finder = Finder()
        url = self.ui.lineEdit.text()
        phrase = self.ui.lineEdit_2.text()
        interval = self.ui.lineEdit_3.text()
        
        finder.set_url(url)
        finder.set_phrase(phrase)
        finder.set_interval(interval)
        
        self.addToTable(finder.isFound(), finder.get_phrase(), self.ui.tableWidget)
        print "save"
        pass
    def setEvents(self):
        self.ui.newButton.clicked.connect(self.newButtonClick)
        self.ui.zvvklButton.clicked.connect(self.zvvklButtonClick)
        self.ui.zvotklButton.clicked.connect(self.zvotklButtonClick)
        self.ui.saveButton.clicked.connect(self.saveButtonClick)
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
        lb2.setAlignment(QtCore.Qt.AlignCenter)
        lb2.setText(header)
        
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
    
    pass

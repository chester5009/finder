from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QIcon
from PyQt4.Qt import QSize
class controller:
    
    def __init__(self,ui,window):
        self.ui=ui
        self.window=window
        self.setIcons()
        
        pass
    
    def setIcons(self):
        button1=self.ui.newButton
        icon=QIcon("assets/new.png")
        button1.setIcon(icon)
        button1.setIconSize(QSize(button1.width(),button1.height()))
        
        button2=self.ui.zvvklButton
        icon=QIcon("assets/zvvkl.png")
        button2.setIcon(icon)
        button2.setIconSize(QSize(button2.width(),button2.height()))
        
        button3=self.ui.zvotklButton
        icon=QIcon("assets/zvotkl.png")
        button3.setIcon(icon)
        button3.setIconSize(QSize(button3.width(),button3.height()))
        
        pass
    pass
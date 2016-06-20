# -*- coding: utf-8 -*-

import sys,urllib,requests
import time
from form import Ui_Form
from PyQt4 import QtCore,QtGui
from PyQt4.Qt import QApplication, QDialog
from controller import controller


sait=urllib.urlopen("https://www.yandex.ru/")

whatfound="Метро"

f=open("index.html",'w')
data=sait.read()
print data
print data.find(whatfound)
f.write(data)
f.close()


def main():
    app = QApplication(sys.argv)
    window=QDialog()
    ui=Ui_Form()
    ui.setupUi(window)
    
    control=controller(ui,window)
    window.show()
    sys.exit(app.exec_())
    pass

if __name__ == '__main__':
    main()
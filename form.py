# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(350, 550)
        Form.setMinimumSize(QtCore.QSize(350, 550))
        Form.setMaximumSize(QtCore.QSize(350, 99999))
        self.newButton = QtGui.QPushButton(Form)
        self.newButton.setGeometry(QtCore.QRect(10, 10, 60, 60))
        self.newButton.setStyleSheet(_fromUtf8("border-image: url(\"/home/chester/Документы/eclipseprojects/GetFromSait/assetsnew.png\");"))
        self.newButton.setText(_fromUtf8(""))
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.zvvklButton = QtGui.QPushButton(Form)
        self.zvvklButton.setGeometry(QtCore.QRect(80, 10, 60, 60))
        self.zvvklButton.setText(_fromUtf8(""))
        self.zvvklButton.setObjectName(_fromUtf8("zvvklButton"))
        self.zvotklButton = QtGui.QPushButton(Form)
        self.zvotklButton.setGeometry(QtCore.QRect(160, 10, 60, 60))
        self.zvotklButton.setText(_fromUtf8(""))
        self.zvotklButton.setObjectName(_fromUtf8("zvotklButton"))
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 80, 311, 431))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.scrollArea = QtGui.QScrollArea(self.page)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 291, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 329))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Finder", None))


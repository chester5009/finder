# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Fri Jun 17 14:52:06 2016
#      by: PyQt4 UI code generator 4.10.4
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
        Form.resize(350, 707)
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
        self.stackedWidget.setGeometry(QtCore.QRect(10, 80, 321, 601))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.lineEdit = QtGui.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(90, 360, 171, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 400, 141, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.page)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 440, 41, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(20, 360, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(20, 400, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(20, 440, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tableWidget = QtGui.QTableWidget(self.page)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 301, 341))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.saveButton = QtGui.QPushButton(self.page)
        self.saveButton.setGeometry(QtCore.QRect(20, 490, 281, 27))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Finder", None))
        self.label.setText(_translate("Form", "Ссылка", None))
        self.label_2.setText(_translate("Form", "Фраза", None))
        self.label_3.setText(_translate("Form", "Интервал(с)", None))
        self.saveButton.setText(_translate("Form", "Сохранить", None))


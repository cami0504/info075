# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hola.ui'
#
# Created: Thu Jun  6 11:50:24 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui



class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 211)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 201, 111))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(20)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Hola Github", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Hola github", None, QtGui.QApplication.UnicodeUTF8))
        


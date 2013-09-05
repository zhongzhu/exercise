# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oneresult.ui'
#
# Created: Thu Sep 05 11:25:19 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(251, 41)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_pic = QtGui.QLabel(Form)
        self.label_pic.setObjectName("label_pic")
        self.horizontalLayout.addWidget(self.label_pic)
        self.label_description = QtGui.QLabel(Form)
        self.label_description.setObjectName("label_description")
        self.horizontalLayout.addWidget(self.label_description)
        self.pushButton_view = QtGui.QPushButton(Form)
        self.pushButton_view.setObjectName("pushButton_view")
        self.horizontalLayout.addWidget(self.pushButton_view)
        self.pushButton_download = QtGui.QPushButton(Form)
        self.pushButton_download.setObjectName("pushButton_download")
        self.horizontalLayout.addWidget(self.pushButton_download)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pic.setText(QtGui.QApplication.translate("Form", "pic", None, QtGui.QApplication.UnicodeUTF8))
        self.label_description.setText(QtGui.QApplication.translate("Form", "description", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view.setText(QtGui.QApplication.translate("Form", "view", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_download.setText(QtGui.QApplication.translate("Form", "Download", None, QtGui.QApplication.UnicodeUTF8))


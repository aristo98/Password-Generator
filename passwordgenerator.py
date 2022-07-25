# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwordgenerator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyperclip import copy
import maincode as mc

class GUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 247)
        MainWindow.setMinimumHeight(247)
        MainWindow.setMaximumHeight(247)
        MainWindow.setMinimumWidth(441)
        MainWindow.setMaximumWidth(441)
        MainWindow.setToolTip("At least one box must be checked")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 401, 189))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(True)
        self.checkBox.setToolTip("a-z")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setToolTip("A-Z")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setToolTip("0-9")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setToolTip("´&<>"+"’"+"'*@\{}[]^¢«»©†°\n"+\
                                   "÷$.–=€!`≤≥\"×≠#()%π|\n"+\
                                       "+±?®§/~™_")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setToolTip("Length of the password")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setToolTip("How many passwords shall be generated")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setToolTip("Type integer between 6-20")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setToolTip("More than one password will be separated by blank spaces")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.clicked.connect(self.create)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setToolTip("Generate password")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setToolTip("Generated editable password")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setToolTip("Copy to clipboard")
        self.pushButton_2.clicked.connect(self.copy_to_clipboard)
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setToolTip("Erase generated password")
        self.pushButton_3.clicked.connect(self.erase)
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def create(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            para,length,numb="",int(self.lineEdit.text()),int(self.lineEdit_2.text())
        except:
            print("Please insert integer in length")
        if self.checkBox.isChecked():
            para+="0"
        if self.checkBox_2.isChecked():
            para+="1"
        if self.checkBox_3.isChecked():
            para+="2"
        if self.checkBox_4.isChecked():
            para+="3"
        cr=mc.Password_Generator(para,length)
        if numb>1:
            passwords=""
            for i in range(numb):
                passwords+=cr.generate_pass()+"\t"
            passwords=passwords[:-1]
            self.lineEdit_3.setText(_translate("MainWindow",passwords))
        else:
            self.lineEdit_3.setText(_translate("MainWindow",cr.generate_pass()))
    
    def copy_to_clipboard(self):
        copy(self.lineEdit_3.text())
    def erase(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit_3.setText(_translate("MainWindow",""))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.checkBox.setText(_translate("MainWindow", "lowercase"))
        self.checkBox_2.setText(_translate("MainWindow", "UPPERCASE"))
        self.checkBox_3.setText(_translate("MainWindow", "Numbers"))
        self.checkBox_4.setText(_translate("MainWindow", "Special characters"))
        self.label.setText(_translate("MainWindow", "Length"))
        self.label_2.setText(_translate("MainWindow", "How many"))
        self.lineEdit.setText(_translate("MainWindow", "8"))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.pushButton_2.setText(_translate("MainWindow", "Copy"))
        self.pushButton_3.setText(_translate("MainWindow", "Erase"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


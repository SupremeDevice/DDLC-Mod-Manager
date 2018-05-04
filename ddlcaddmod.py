# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ddlc add mod dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os, sys, configparser, shutil


class Ui_AddMod(object):
    def setupUi(self, AddMod, n):
        global gameFld
        gameFld = n
        AddMod.setObjectName("AddMod")
        AddMod.resize(491, 145)
        AddMod.setMaximumSize(QtCore.QSize(16777215, 200))
        self.gridLayout = QtWidgets.QGridLayout(AddMod)
        self.gridLayout.setObjectName("gridLayout")
        self.imagesrpaCheck = QtWidgets.QCheckBox(AddMod)
        self.imagesrpaCheck.setObjectName("imagesrpaCheck")
        self.gridLayout.addWidget(self.imagesrpaCheck, 3, 0, 1, 1)
        self.nameInputLabel = QtWidgets.QLabel(AddMod)
        self.nameInputLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.nameInputLabel.setObjectName("nameInputLabel")
        self.gridLayout.addWidget(self.nameInputLabel, 0, 0, 1, 1)
        self.modAddBtns = QtWidgets.QDialogButtonBox(AddMod)
        self.modAddBtns.setOrientation(QtCore.Qt.Horizontal)
        self.modAddBtns.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.modAddBtns.setObjectName("modAddBtns")
        self.gridLayout.addWidget(self.modAddBtns, 5, 0, 1, 1)
        self.nameInputEdit = QtWidgets.QLineEdit(AddMod)
        self.nameInputEdit.setObjectName("nameInputEdit")
        self.gridLayout.addWidget(self.nameInputEdit, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(AddMod)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)

        self.retranslateUi(AddMod)

        self.modAddBtns.accepted.connect(self.addMod)

        self.modAddBtns.rejected.connect(AddMod.close)

        QtCore.QMetaObject.connectSlotsByName(AddMod)

    def retranslateUi(self, AddMod):
        _translate = QtCore.QCoreApplication.translate
        AddMod.setWindowTitle(_translate("AddMod", "Dialog"))
        self.imagesrpaCheck.setText(_translate("AddMod", "Use v1.1.0\'s image.rpa\n"
"(Maximise compatibility for mods before April 8th)"))
        self.nameInputLabel.setText(_translate("AddMod", "Name:"))
        self.checkBox.setText(_translate("AddMod", "Extract Base Game Scripts"))


    def addMod(self):
        print("getting name of new mod")
        newName = self.nameInputEdit.text()
#        newName = "oofers"
        if newName == (""):
            QMessageBox.question(None, 'Error', "Please input a name for the new mod.", QMessageBox.Ok)
        else:
            print(newName)
            #newDir = bytes(newName, 'utf-8').decode('utf-8', 'ignore')
            global newDir
            newDir = newName
            newDir = "".join(i for i in newDir if i not in "\/:*?<>|")
            if newDir != newName:
                #print("Error, folder name will be changed to " + newDir + " from " + newName)
                proceed = QMessageBox.question(None, 'Warning', "Folder name will be changed to '" + newDir + "' from '" + newName + "'", QMessageBox.Ok | QMessageBox.Cancel)
                if proceed == QMessageBox.Ok:
                    self.createDir()
            else:
#                print(newDir)
                print("Directory name is valid")
                self.createDir()


    def createDir(self):
        global newDir
        newDir = os.path.join(os.getcwd(), "mods", newDir)
        print(newDir)
        if not os.path.exists(newDir):
            print("Copying DDLC to mod folder")
            shutil.copytree(gameFld, newDir)
            os.startfile(newDir)
            self.reloadDDLC()
        else:
            proceed = QMessageBox.question(None, 'Confirm', "Folder already exists, do you wish to proceed?", QMessageBox.Yes | QMessageBox.No)
            if proceed == QMessageBox.Yes:
                print("Proceed anyways")
                shutil.rmtree(newDir)
                print('Removing ' + newDir)
                print("Copying DDLC to mod folder")
                shutil.copytree(gameFld, newDir)
                os.startfile(newDir)
            else:
                pass

    def reloadDDLC(self):
        os.startfile('ddlc.py')
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddMod = QtWidgets.QDialog()
    ui = Ui_AddMod()
    ui.setupUi(AddMod)
    AddMod.show()
    sys.exit(app.exec_())

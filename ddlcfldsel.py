# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ddlc folder selector.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
import configparser
import io

class Ui_Fld_Sel(object):

    def setupUi(self, Fld_Sel):
        global gameFld
        config = configparser.ConfigParser(allow_no_value=True)
        config.read('config.ini')
        gameFld = config['DEFAULT']['ddlcfolder']
#        print(gameFld)




        Fld_Sel.setObjectName("Fld_Sel")
        Fld_Sel.resize(546, 170)
        Fld_Sel.setMaximumSize(QtCore.QSize(16777215, 170))
        Fld_Sel.setWhatsThis("")
        self.gridLayout = QtWidgets.QGridLayout(Fld_Sel)
        self.gridLayout.setObjectName("gridLayout")
        self.openDirectory110 = QtWidgets.QToolButton(Fld_Sel)
        self.openDirectory110.setObjectName("openDirectory110")
        self.gridLayout.addWidget(self.openDirectory110, 1, 3, 1, 1)
#Open DDLC/game folder if images-110.rpa is inside
        self.openDirectory110.clicked.connect(self.openGameFld)


        self.chooseDirectory111 = QtWidgets.QToolButton(Fld_Sel)
        self.chooseDirectory111.setCheckable(False)
        self.chooseDirectory111.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.chooseDirectory111.setObjectName("chooseDirectory111")
        self.gridLayout.addWidget(self.chooseDirectory111, 3, 3, 1, 1)
#Choose folder that DDLC is stored in
        self.chooseDirectory111.clicked.connect(self.chsFld)


        self.folderPath111 = QtWidgets.QLineEdit(Fld_Sel)
        self.folderPath111.setInputMask("")
        self.folderPath111.setText("")
        self.folderPath111.setObjectName("folderPath111")
        self.gridLayout.addWidget(self.folderPath111, 3, 1, 1, 1)
        self.folderLabel110 = QtWidgets.QLabel(Fld_Sel)
        self.folderLabel110.setMaximumSize(QtCore.QSize(16777215, 24))
        self.folderLabel110.setObjectName("folderLabel110")
        self.gridLayout.addWidget(self.folderLabel110, 0, 1, 1, 1)
        self.folderLabel111 = QtWidgets.QLabel(Fld_Sel)
        self.folderLabel111.setMaximumSize(QtCore.QSize(16777215, 24))
        self.folderLabel111.setObjectName("folderLabel111")
        self.gridLayout.addWidget(self.folderLabel111, 2, 1, 1, 1)
        self.imagesPathLabel = QtWidgets.QLabel(Fld_Sel)
        self.imagesPathLabel.setObjectName("imagesPathLabel")
        self.gridLayout.addWidget(self.imagesPathLabel, 1, 1, 1, 1)

        self.retranslateUi(Fld_Sel)
        QtCore.QMetaObject.connectSlotsByName(Fld_Sel)

    def retranslateUi(self, Fld_Sel):
        _translate = QtCore.QCoreApplication.translate
        Fld_Sel.setWindowTitle(_translate("Fld_Sel", "Download DDLC"))
        self.openDirectory110.setText(_translate("Fld_Sel", "..."))
        self.chooseDirectory111.setText(_translate("Fld_Sel", "..."))
        self.folderPath111.setPlaceholderText(_translate("Fld_Sel", "Choose which folder v1.1.1 is located."))
#Set it to display game folder if set in config.ini
        if gameFld != None:
            self.folderPath111.setText(gameFld)


        self.folderLabel110.setText(_translate("Fld_Sel", "DDLC v1.1.0 images.rpa Location:"))
        self.folderLabel111.setText(_translate("Fld_Sel", "DDLC v1.1.1 Location:"))
        self.imagesPathLabel.setText(_translate("Fld_Sel", "images-110.rpa does not exist or is not in DDLC/game/"))

    def chsFld(self):
        global gameFld
        tempFld = str(QFileDialog.getExistingDirectory(None, "Choose Directory"))
        if tempFld != '':
            print(tempFld)
            gameFld = tempFld
            #Update text on folder selector dialog to reflect new location
            self.folderPath111.setText(gameFld)
            #Save new game directory to config.ini
            config = configparser.ConfigParser(allow_no_value=True)
            config.read('config.ini')
            config['DEFAULT']['ddlcfolder'] = gameFld

            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        else:
            pass

    def openGameFld(self):
#        print("niceu")
        try:
            if gameFld != None:
#Checking if a location for DDLC has been set
#                print("niceur")
                if os.path.join(gameFld, "game") != None:
                    os.startfile(os.path.join(gameFld, "game"))
#Checking if DDLC installation is valid, i.e. does it have a "game" folder
        except WindowsError:
            print("No 'game' folder, reinstall DDLC")
            QMessageBox.question(None, 'Error', "There is no '/DDLC/game' folder or DDLC location is incorrect, reinstall DDLC.", QMessageBox.Ok)
        except NameError:
            print("No location set for DDLC")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fld_Sel = QtWidgets.QDialog()
    ui = Ui_Fld_Sel()
    ui.setupUi(Fld_Sel)
    Fld_Sel.show()
    sys.exit(app.exec_())

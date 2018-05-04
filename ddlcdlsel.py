# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ddlc download selector.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ddlcdlsel2 import Ui_dlMethod
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
import configparser


class Ui_DL_Sel(object):

    #defining global variables to check what needs to be downloaded
    global dlImages
    dlImages = False
    global dlDDLC
    dlDDLC = False


    def openDl_Prg(self):
        import urllib
        from urllib import request
        global dlTest
        dlTest = 0
        if dlDDLC == True:
            dlTest += 1
            try:
                if gameFld != '':
                    print(gameFld)
                    print("wow you should save your config here :)")
            except NameError:
                print("Using default path")

            print("dlDDLC = true, opening dl method selection Dialog")
            self.window = QtWidgets.QWidget()
            self.ui = Ui_dlMethod()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            pass

        if dlImages == True:
            dlTest += 1
            print("dlImages = true, downloading images-110.rpa")
            url = "http://drive.google.com/uc?export=download&id=1rfE66WybJiF7XKHH0-NGksTyXa6Gt3xh"
            urllib.request.urlretrieve(url, os.path.join(os.getcwd(), 'temp\images-110.rpa'))
        else:
            pass
        if dlTest == 0:
            QMessageBox.question(None, 'Error', "Please select one of the checkboxes first.", QMessageBox.Ok)


    def setupUi(self, DL_Sel):
        DL_Sel.setObjectName("DL_Sel")
        DL_Sel.resize(550, 187)
        DL_Sel.setMaximumSize(QtCore.QSize(16777215, 250))
        DL_Sel.setWhatsThis("")
        self.gridLayout = QtWidgets.QGridLayout(DL_Sel)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonDownload = QtWidgets.QPushButton(DL_Sel)
        self.buttonDownload.setObjectName("buttonDownload")
		#Open DL Progress Dialog
        self.buttonDownload.clicked.connect(self.openDl_Prg)
        self.gridLayout.addWidget(self.buttonDownload, 9, 1, 1, 1)
        self.savePath111 = QtWidgets.QLineEdit(DL_Sel)
        self.savePath111.setInputMask("")
        self.savePath111.setText("")
        self.savePath111.setObjectName("savePath111")
        self.gridLayout.addWidget(self.savePath111, 2, 1, 1, 1)
        self.checkDownload110 = QtWidgets.QCheckBox(DL_Sel)
        self.checkDownload110.setObjectName("checkDownload110")
        self.gridLayout.addWidget(self.checkDownload110, 0, 1, 1, 1)
#       Set images-110.rpa to be downloaded
        self.checkDownload110.clicked.connect(self.chkImages)


        self.chooseDirectory111 = QtWidgets.QToolButton(DL_Sel)
        self.chooseDirectory111.setCheckable(False)
        self.chooseDirectory111.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.chooseDirectory111.setObjectName("chooseDirectory111")
        self.gridLayout.addWidget(self.chooseDirectory111, 2, 3, 1, 1)
#       Select folder to save DDLC, same code as in ddlcfldsel.py
        self.chooseDirectory111.clicked.connect(self.chsFld)

        self.checkDownload111 = QtWidgets.QCheckBox(DL_Sel)
        self.checkDownload111.setObjectName("checkDownload111")
        self.gridLayout.addWidget(self.checkDownload111, 1, 1, 1, 1)
#       Set DDLCv1.1.1 to be downloaded
        self.checkDownload111.clicked.connect(self.chkDDLC)


        self.retranslateUi(DL_Sel)
        QtCore.QMetaObject.connectSlotsByName(DL_Sel)

    def retranslateUi(self, DL_Sel):
        _translate = QtCore.QCoreApplication.translate
        DL_Sel.setWindowTitle(_translate("DL_Sel", "Download DDLC"))

        #Fix button after implementing obvs
        self.buttonDownload.setText(_translate("DL_Sel", "Download (Not Implemented Yet)"))
        self.savePath111.setPlaceholderText(_translate("DL_Sel", "Choose where to place after download. Leave blank for default location in Mod Manager folder."))
        self.checkDownload110.setText(_translate("DL_Sel", " Download DDLC 1.1.0 images.rpa"))
        self.chooseDirectory111.setText(_translate("DL_Sel", "..."))
        self.checkDownload111.setText(_translate("DL_Sel", " Download DDLC 1.1.1"))

    def chsFld(self):
        global gameFld
        tempFld = str(QFileDialog.getExistingDirectory(None, "Choose Directory"))
        if tempFld != '':
            print(tempFld)
            gameFld = tempFld
            #Update text on folder selector dialog to reflect new location
            self.savePath111.setText(gameFld)
            #Save new game directory to config.ini
            config = configparser.ConfigParser(allow_no_value=True)
            config.read('config.ini')
            config['DEFAULT']['ddlcfolder'] = gameFld

            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        else:
            pass


#Toggles either dlImages or dlDDLC
    def chkImages(self):
        global dlImages
        dlImages = not dlImages
        #print(dlImages)
        self.chkStatus()

    def chkDDLC(self):
        global dlDDLC
        dlDDLC = not dlDDLC
        self.chkStatus()


    def chkStatus(self):
    #    global dlImages
    #    global dlDDLC
        print(dlDDLC)
        print(dlImages)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DL_Sel = QtWidgets.QDialog()
    ui = Ui_DL_Sel()
    ui.setupUi(DL_Sel)
    DL_Sel.show()
    sys.exit(app.exec_())

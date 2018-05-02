# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ddlc modmanager.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ddlcdlsel import Ui_DL_Sel
from ddlcaddmod import Ui_AddMod
from ddlcfldsel import Ui_Fld_Sel


class Ui_DDLCModManager(QMainWindow):
    def openDl_Sel(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_DL_Sel()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAddMod(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_AddMod()
        self.ui.setupUi(self.window)
        self.window.show()

    def openFld_Sel(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Fld_Sel()
        self.ui.setupUi(self.window)
        self.window.show()

    def rmv_ModPopup(self):
        rmvChoice = QMessageBox.question(self, 'Confirm', "Are you sure you wish to permanently remove this mod?", QMessageBox.Yes | QMessageBox.Cancel)
        if rmvChoice == QMessageBox.Yes:
            print("Removing Mod...")
        else:
            pass

    def setupUi(self, DDLCModManager):
        DDLCModManager.setObjectName("DDLCModManager")
        DDLCModManager.resize(398, 506)
        DDLCModManager.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(DDLCModManager)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.DDLCModList = QtWidgets.QListView(self.centralwidget)
        self.DDLCModList.setObjectName("DDLCModList")
        self.gridLayout.addWidget(self.DDLCModList, 1, 0, 21, 1)
        self.addMod = QtWidgets.QPushButton(self.centralwidget)
        self.addMod.setObjectName("addMod")

		#Open Add Mod menu
        self.addMod.clicked.connect(self.openAddMod)

        self.gridLayout.addWidget(self.addMod, 2, 1, 1, 1)
        self.removeMod = QtWidgets.QPushButton(self.centralwidget)
        self.removeMod.setObjectName("removeMod")

		#Open Warning before doing anything
        self.removeMod.clicked.connect(self.rmv_ModPopup)

        self.gridLayout.addWidget(self.removeMod, 3, 1, 1, 1)
        self.ddlcDownload = QtWidgets.QPushButton(self.centralwidget)
        self.ddlcDownload.setObjectName("ddlcDownload")
		#Open DL Selector
        self.ddlcDownload.clicked.connect(self.openDl_Sel)

        self.gridLayout.addWidget(self.ddlcDownload, 7, 1, 1, 1)
        self.playBtn = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn.setObjectName("playBtn")
        self.gridLayout.addWidget(self.playBtn, 1, 1, 1, 1)
        self.setBaseFolder = QtWidgets.QPushButton(self.centralwidget)
        self.setBaseFolder.setObjectName("setBaseFolder")
		#Open Base Folder Selector
        self.setBaseFolder.clicked.connect(self.openFld_Sel)

        self.gridLayout.addWidget(self.setBaseFolder, 8, 1, 1, 1)
        self.copyMod = QtWidgets.QPushButton(self.centralwidget)
        self.copyMod.setObjectName("copyMod")
        self.gridLayout.addWidget(self.copyMod, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 9, 1, 1, 1)
        DDLCModManager.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DDLCModManager)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 21))
        self.menubar.setObjectName("menubar")
        self.menuUpdates = QtWidgets.QMenu(self.menubar)
        self.menuUpdates.setObjectName("menuUpdates")
        DDLCModManager.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DDLCModManager)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        DDLCModManager.setStatusBar(self.statusbar)
        self.actionCheck_for_Updates = QtWidgets.QAction(DDLCModManager)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.actionView_Source = QtWidgets.QAction(DDLCModManager)
        self.actionView_Source.setObjectName("actionView_Source")
        self.actionInfo = QtWidgets.QAction(DDLCModManager)
        self.actionInfo.setObjectName("actionInfo")
        self.menuUpdates.addAction(self.actionCheck_for_Updates)
        self.menuUpdates.addAction(self.actionView_Source)
        self.menuUpdates.addAction(self.actionInfo)
        self.menubar.addAction(self.menuUpdates.menuAction())

        self.retranslateUi(DDLCModManager)
        QtCore.QMetaObject.connectSlotsByName(DDLCModManager)

    def retranslateUi(self, DDLCModManager):
        _translate = QtCore.QCoreApplication.translate
        DDLCModManager.setWindowTitle(_translate("DDLCModManager", "DDLC Mod Manager"))
        self.addMod.setText(_translate("DDLCModManager", "Add Mod"))
        self.removeMod.setText(_translate("DDLCModManager", "Remove Mod"))
        self.ddlcDownload.setText(_translate("DDLCModManager", "Download\n"
" DDLC"))
        self.playBtn.setText(_translate("DDLCModManager", "Play"))
        self.setBaseFolder.setText(_translate("DDLCModManager", "Set DDLC\n"
" Base Folder"))
        self.copyMod.setText(_translate("DDLCModManager", "Copy Mod"))
        self.pushButton.setText(_translate("DDLCModManager", "Rename Mod"))
        self.pushButton_2.setText(_translate("DDLCModManager", "Open Mod\n"
"Folder"))
        self.menuUpdates.setTitle(_translate("DDLCModManager", "Options"))
        self.actionCheck_for_Updates.setText(_translate("DDLCModManager", "Check for Updates"))
        self.actionView_Source.setText(_translate("DDLCModManager", "View Source"))
        self.actionInfo.setText(_translate("DDLCModManager", "Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DDLCModManager = QtWidgets.QMainWindow()
    ui = Ui_DDLCModManager()
    ui.setupUi(DDLCModManager)
    DDLCModManager.show()
    sys.exit(app.exec_())

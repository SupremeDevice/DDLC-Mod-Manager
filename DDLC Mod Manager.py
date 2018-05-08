#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ddlc modmanager.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from ddlcdlsel import Ui_DL_Sel
from ddlcaddmod import Ui_AddMod
from ddlcfldsel import Ui_Fld_Sel
import os, shutil, configparser, io, platform
import time


class Ui_DDLCModManager(QMainWindow):

    def openDl_Sel(self):
        dialog = QDialog()
        dialog.ui = Ui_DL_Sel()
        dialog.ui.setupUi(dialog)
        if dialog.exec_():
            pass

    def openAddMod(self):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read('config.ini')
        gameFld = config['DEFAULT']['ddlcfolder']
        if os.path.exists(gameFld):
            dialog = QDialog()
            dialog.ui = Ui_AddMod()
            dialog.ui.setupUi(dialog, gameFld)
            if dialog.exec_():
                print("Mod added, refreshing.")
                self.refreshList()
        else:
            QMessageBox.question(self, 'Error', "Please download DDLC or set base game folder location first.", QMessageBox.Ok)


    def openFld_Sel(self):
        dialog = QDialog()
        dialog.ui = Ui_Fld_Sel()
        dialog.ui.setupUi(dialog)
        if dialog.exec_():
            pass

#Gets selected mod of the list
    def on_change(self):
        global currentMod
        currentMod = (', '.join([item.text() for item in self.DDLCModList.selectedItems()]))
        print(currentMod)

    def playMod(self):
        try:
            if currentMod != '':
                if curOS == "Darwin":
                    print("wow you're actually using this on a mac? nice! if only I had one I could test on heh")
                else:
                    gameDir = os.path.join(basemmDir, "mods", currentMod)
                    if curOS == "Windows":
                        os.startfile(os.path.join(gameDir, "DDLC.exe"))
                    elif curOS == "Linux":
                        os.startfile(os.path.join(gameDir, "DDLC.sh"))
                    else:
                        QMessageBox.question(self, 'Error', "Sorry, you have an unknown OS. Please launch DDLC maually from " + os.path.join(basemmDir, "mods"), QMessageBox.Ok)
        except NameError:
            QMessageBox.question(self, 'Error', "Please select a mod to play first.", QMessageBox.Ok)

    def rmv_ModPopup(self):
        try:
            #Make sure a mod has been selected
            if currentMod != '':
                rmvChoice = QMessageBox.question(self, 'Confirm', "Are you sure you wish to permanently remove this mod?", QMessageBox.Yes | QMessageBox.Cancel)
                if rmvChoice == QMessageBox.Yes:
                    print("Removing Mod '" + currentMod + "'")
                    shutil.rmtree(os.path.join(basemmDir, "mods", currentMod))
                    print(os.path.join(basemmDir, "mods", currentMod))
                    #Refresh mod list after deleting mod
                    self.refreshList()
        except NameError:
            QMessageBox.question(self, 'Error', "Please select a mod to remove first.", QMessageBox.Ok)

    def copyModFld(self):
        try:
            #Make sure a mod has been selected
            if currentMod != '':
                srcFld = os.path.join(basemmDir, "mods", currentMod)
                dstFld = (srcFld + " - Copy")
                shutil.copytree(srcFld, dstFld)
                #Refresh mod list to include copy
                self.refreshList()
#                print(currentMod)
            else:
                QMessageBox.question(self, 'Error', "Please select a mod to copy first.", QMessageBox.Ok)
        except NameError:
            QMessageBox.question(self, 'Error', "Please select a mod to copy first.", QMessageBox.Ok)
        except FileExistsError:
            self.forceCopy(dstFld, srcFld)

    def renameMod(self):
        try:
            #Make sure a mod has been selected
            if currentMod != '':
                #Get mod's new name
                newName, okPressed = QInputDialog.getText(self, "Rename Mod","New Name:", QLineEdit.Normal, "")
                if okPressed and newName != '':
                    newDir = newName
                    newDir = "".join(i for i in newDir if i not in "\/:*?<>|")
                    if newDir != newName:
                        #print("Error, folder name will be changed to " + newDir + " from " + newName)
                        proceed = QMessageBox.question(None, 'Warning', "Folder name will be changed to '" + newDir + "' instead of '" + newName + "'", QMessageBox.Ok | QMessageBox.Cancel)
                        if proceed == QMessageBox.Ok:
                            self.renameReally(newDir)
                    else:
                        self.renameReally(newDir)
            else:
                QMessageBox.question(self, 'Error', "Please select a mod to rename first.", QMessageBox.Ok)
        except NameError:
            QMessageBox.question(self, 'Error', "Please select a mod to rename first.", QMessageBox.Ok)
        except FileExistsError:
            QMessageBox.question(self, 'Error', "That name is already being used.", QMessageBox.Ok)

    def renameReally(self, n):
        srcFld = os.path.join(basemmDir, "mods", currentMod)
        dstFld = os.path.join(basemmDir, "mods", n)
        os.rename(srcFld, dstFld)
                #Refresh mod list to reflect new name
        self.refreshList()


    def forceCopy(self, n, srcFld):
        try:
            dstFld = (n + " - Copy")
            shutil.copytree(srcFld, dstFld)
            self.refreshList()
        except FileExistsError:
            self.forceCopy(dstFld, srcFld)

    def openModFld(self):
        try:
            #Make sure a mod has been selected
            if currentMod != '':
                gameFld = os.path.join(basemmDir, "mods", currentMod)
                if curOS == 'Windows':
                    os.startfile(gameFld)
                elif curOS == 'Linux':
                    os.system("xdg-open " + gameFld)
                elif curOS == 'Darwin':
                    os.system("open " + gameFld)
            else:
                QMessageBox.question(self, 'Error', "Please select a mod to browse first.", QMessageBox.Ok)
        except NameError:
            QMessageBox.question(self, 'Error', "Please select a mod to browse first.", QMessageBox.Ok)

    def setupUi(self, DDLCModManager):
        global ddlcmmui
        ddlcmmui = self
        global curOS
        curOS = platform.system()

        DDLCModManager.setObjectName("DDLCModManager")
        DDLCModManager.resize(398, 506)
        DDLCModManager.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(DDLCModManager)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.DDLCModList = QtWidgets.QListWidget(self.centralwidget)
        self.DDLCModList.setObjectName("DDLCModList")
        self.gridLayout.addWidget(self.DDLCModList, 1, 0, 21, 1)
#Get mod folders to list
        self.getMods()

#Get current mod choice
        self.DDLCModList.itemSelectionChanged.connect(self.on_change)

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
        #Play selected mod
        self.playBtn.clicked.connect(self.playMod)

        self.setBaseFolder = QtWidgets.QPushButton(self.centralwidget)
        self.setBaseFolder.setObjectName("setBaseFolder")
		#Open Base Folder Selector
        self.setBaseFolder.clicked.connect(self.openFld_Sel)

        self.gridLayout.addWidget(self.setBaseFolder, 8, 1, 1, 1)
        self.copyMod = QtWidgets.QPushButton(self.centralwidget)
        self.copyMod.setObjectName("copyMod")
        self.gridLayout.addWidget(self.copyMod, 4, 1, 1, 1)
        #Guess what this does!
        self.copyMod.clicked.connect(self.copyModFld)

        self.renameModBtn = QtWidgets.QPushButton(self.centralwidget)
        self.renameModBtn.setObjectName("pushButton")
        self.gridLayout.addWidget(self.renameModBtn, 5, 1, 1, 1)
        #You know the drill
        self.renameModBtn.clicked.connect(self.renameMod)

        self.openModBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openModBtn.setObjectName("openModBtn")
        self.gridLayout.addWidget(self.openModBtn, 9, 1, 1, 1)
        self.openModBtn.clicked.connect(self.openModFld)

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
        #open up link to github source
        self.actionView_Source.triggered.connect(self.clkSource)

        self.actionInfo = QtWidgets.QAction(DDLCModManager)
        self.actionInfo.setObjectName("actionInfo")
        #open up info box
        self.actionInfo.triggered.connect(self.clkInfo)

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
        self.renameModBtn.setText(_translate("DDLCModManager", "Rename Mod"))
        self.openModBtn.setText(_translate("DDLCModManager", "Open Mod\n"
"Folder"))
        self.menuUpdates.setTitle(_translate("DDLCModManager", "Options"))
        self.actionCheck_for_Updates.setText(_translate("DDLCModManager", "Check for Updates"))
        self.actionView_Source.setText(_translate("DDLCModManager", "View Source"))
        self.actionInfo.setText(_translate("DDLCModManager", "Info"))

    def clkSource(self):
        print("source button clicked")
        if curOS == "Windows":
            os.system("start https://github.com/SupremeDevice/DDLC-Mod-Manager")
        if curOS == "Linux":
            os.system("xdg-open https://github.com/SupremeDevice/DDLC-Mod-Manager")
        if curOS == "Darwin":
            os.system("open https://github.com/SupremeDevice/DDLC-Mod-Manager")

    def clkInfo(self):
        QMessageBox.about(self, "Info", "DDLC Mod Manager v1.0\nDeveloped by SupremeDevice\nNot affiliated with Team Salvato")

    def getMods(self):
        next(os.walk('.'))[1]
        global basemmDir
        basemmDir = os.getcwd()
#        print(basemmDir)
#        print(os.path.join(basemmDir, "temp"))
        print(os.path.join(basemmDir, "mods"))
        #print(basemmDir)
        os.chdir(os.path.join(os.getcwd(), "mods"))
        #next(os.walk('.'))[1]
        print(os.listdir(os.path.join(basemmDir, "mods")))
#        print(next)
        self.DDLCModList.addItems(os.listdir(os.path.join(basemmDir, "mods")))
#        self.DDLCModList = QtWidgets.QListView(os.listdir(os.path.join(basemmDir, "mods")))
        os.chdir(basemmDir)
        print(os.getcwd())

    def refreshList(self):
        self.DDLCModList.clear()
        self.DDLCModList.addItems(os.listdir(os.path.join(basemmDir, "mods")))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.png'))
    DDLCModManager = QtWidgets.QMainWindow()
    ui = Ui_DDLCModManager()
    ui.setupUi(DDLCModManager)
    DDLCModManager.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ddlc download progress.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DL_Prg(object):
#    dlBarValue = 0
 #   def setDLPrg(n):
 #       dlBarValue = n
	#	
    global dlBarValue
    dlBarValue = 20
    global name
    name = "Downloading DDLC..."
    def setupUi(self, DL_Prg):
        DL_Prg.setObjectName("DL_Prg")
        DL_Prg.resize(369, 180)
        DL_Prg.setMaximumSize(QtCore.QSize(16777215, 180))
        DL_Prg.setWindowOpacity(1.0)
        self.verticalLayout = QtWidgets.QVBoxLayout(DL_Prg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.downloadLabel = QtWidgets.QLabel(DL_Prg)
        self.downloadLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.downloadLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.downloadLabel.setWordWrap(False)
        self.downloadLabel.setObjectName("downloadLabel")
        self.verticalLayout.addWidget(self.downloadLabel)
        self.downloadBar = QtWidgets.QProgressBar(DL_Prg)
        self.downloadBar.setProperty("value", dlBarValue)
        self.downloadBar.setObjectName("downloadBar")
        self.verticalLayout.addWidget(self.downloadBar)
        #print(self.dlBarValue)
        self.retranslateUi(DL_Prg)
        QtCore.QMetaObject.connectSlotsByName(DL_Prg)

    def barUpdate(self, n):
        self.downloadBar.setProperty("value", n)

    def nameUpdate(self, n):
        name = n
        Ui_DL_Prg().nameChange(QtWidgets.QDialog())
        print(name)
	
    def retranslateUi(self, DL_Prg):
        _translate = QtCore.QCoreApplication.translate
        DL_Prg.setWindowTitle(name)
        #DL_Prg.setWindowTitle('Checkbox')
        self.downloadLabel.setText(_translate("DL_Prg", "Downloading DDLC..."))

    def nameChange(self):
        QtWidgets.QDialog().setWindowTitle("new name nice")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DL_Prg = QtWidgets.QDialog()
    ui = Ui_DL_Prg()
    ui.setupUi(DL_Prg)
    DL_Prg.show()
    sys.exit(app.exec_())


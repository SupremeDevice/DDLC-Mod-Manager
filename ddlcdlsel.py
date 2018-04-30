# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ddlc download selector.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ddlcdlprg import Ui_DL_Prg

class Ui_DL_Sel(object):
    def openDl_Prg(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_DL_Prg()
        self.ui.setupUi(self.window)
        self.window.show()
		
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
        self.chooseDirectory111 = QtWidgets.QToolButton(DL_Sel)
        self.chooseDirectory111.setCheckable(False)
        self.chooseDirectory111.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.chooseDirectory111.setObjectName("chooseDirectory111")
        self.gridLayout.addWidget(self.chooseDirectory111, 2, 3, 1, 1)
        self.checkDownload111 = QtWidgets.QCheckBox(DL_Sel)
        self.checkDownload111.setObjectName("checkDownload111")
        self.gridLayout.addWidget(self.checkDownload111, 1, 1, 1, 1)

        self.retranslateUi(DL_Sel)
        QtCore.QMetaObject.connectSlotsByName(DL_Sel)

    def retranslateUi(self, DL_Sel):
        _translate = QtCore.QCoreApplication.translate
        DL_Sel.setWindowTitle(_translate("DL_Sel", "Download DDLC"))
        self.buttonDownload.setText(_translate("DL_Sel", "Download"))
        self.savePath111.setPlaceholderText(_translate("DL_Sel", "Choose where to place after download. Leave blank for default location in Mod Manager folder."))
        self.checkDownload110.setText(_translate("DL_Sel", " Download DDLC 1.1.0 images.rpa"))
        self.chooseDirectory111.setText(_translate("DL_Sel", "..."))
        self.checkDownload111.setText(_translate("DL_Sel", " Download DDLC 1.1.1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DL_Sel = QtWidgets.QDialog()
    ui = Ui_DL_Sel()
    ui.setupUi(DL_Sel)
    DL_Sel.show()
    sys.exit(app.exec_())


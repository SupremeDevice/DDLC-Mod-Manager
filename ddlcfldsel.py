# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ddlc folder selector.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Fld_Sel(object):
    def setupUi(self, Fld_Sel):
        Fld_Sel.setObjectName("Fld_Sel")
        Fld_Sel.resize(550, 170)
        Fld_Sel.setMaximumSize(QtCore.QSize(16777215, 170))
        Fld_Sel.setWhatsThis("")
        self.gridLayout = QtWidgets.QGridLayout(Fld_Sel)
        self.gridLayout.setObjectName("gridLayout")
        self.chooseDirectory110 = QtWidgets.QToolButton(Fld_Sel)
        self.chooseDirectory110.setObjectName("chooseDirectory110")
        self.gridLayout.addWidget(self.chooseDirectory110, 1, 3, 1, 1)
        self.folderPath110 = QtWidgets.QLineEdit(Fld_Sel)
        self.folderPath110.setText("")
        self.folderPath110.setObjectName("folderPath110")
        self.gridLayout.addWidget(self.folderPath110, 1, 1, 1, 1)
        self.chooseDirectory111 = QtWidgets.QToolButton(Fld_Sel)
        self.chooseDirectory111.setCheckable(False)
        self.chooseDirectory111.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.chooseDirectory111.setObjectName("chooseDirectory111")
        self.gridLayout.addWidget(self.chooseDirectory111, 3, 3, 1, 1)
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

        self.retranslateUi(Fld_Sel)
        QtCore.QMetaObject.connectSlotsByName(Fld_Sel)

    def retranslateUi(self, Fld_Sel):
        _translate = QtCore.QCoreApplication.translate
        Fld_Sel.setWindowTitle(_translate("Fld_Sel", "Download DDLC"))
        self.chooseDirectory110.setText(_translate("Fld_Sel", "..."))
        self.folderPath110.setPlaceholderText(_translate("Fld_Sel", "Choose which folder v1.1.0\'s image.rpa is located."))
        self.chooseDirectory111.setText(_translate("Fld_Sel", "..."))
        self.folderPath111.setPlaceholderText(_translate("Fld_Sel", "Choose which folder v1.1.1 is located."))
        self.folderLabel110.setText(_translate("Fld_Sel", "DDLC v1.1.0 images.rpa Location"))
        self.folderLabel111.setText(_translate("Fld_Sel", "DDLC v1.1.1 Location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fld_Sel = QtWidgets.QDialog()
    ui = Ui_Fld_Sel()
    ui.setupUi(Fld_Sel)
    Fld_Sel.show()
    sys.exit(app.exec_())


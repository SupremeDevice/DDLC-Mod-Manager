# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ddlc add mod dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddMod(object):
    def setupUi(self, AddMod):
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
#
#Disabled to get launching working in the meantime. Don't forget to implement before release
#
#        self.modAddBtns.accepted.connect(AddMod.accept)
#        self.modAddBtns.rejected.connect(AddMod.reject)
        QtCore.QMetaObject.connectSlotsByName(AddMod)

    def retranslateUi(self, AddMod):
        _translate = QtCore.QCoreApplication.translate
        AddMod.setWindowTitle(_translate("AddMod", "Dialog"))
        self.imagesrpaCheck.setText(_translate("AddMod", "Use v1.1.0\'s image.rpa\n"
"(Maximise compatibility for mods before April 8th)"))
        self.nameInputLabel.setText(_translate("AddMod", "Name:"))
        self.checkBox.setText(_translate("AddMod", "Extract Base Game Scripts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddMod = QtWidgets.QDialog()
    ui = Ui_AddMod()
    ui.setupUi(AddMod)
    AddMod.show()
    sys.exit(app.exec_())


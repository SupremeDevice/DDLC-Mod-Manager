# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ddlc download method.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import configparser
import platform

class Ui_dlMethod(object):
    def setupUi(self, dlMethod):
        dlMethod.setObjectName("dlMethod")
        dlMethod.resize(440, 180)
        dlMethod.setMaximumSize(QtCore.QSize(440, 180))
        self.gridLayout = QtWidgets.QGridLayout(dlMethod)
        self.gridLayout.setObjectName("gridLayout")
        self.radioFirefox = QtWidgets.QRadioButton(dlMethod)
        self.radioFirefox.setChecked(False)
        self.radioFirefox.setObjectName("radioFirefox")
        self.gridLayout.addWidget(self.radioFirefox, 2, 0, 1, 1)
        self.radioChrome = QtWidgets.QRadioButton(dlMethod)
        self.radioChrome.setObjectName("radioChrome")
        self.gridLayout.addWidget(self.radioChrome, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(dlMethod)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.radioManual = QtWidgets.QRadioButton(dlMethod)
        self.radioManual.setObjectName("radioManual")
        self.gridLayout.addWidget(self.radioManual, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(dlMethod)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(dlMethod)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 2)

        self.retranslateUi(dlMethod)
        QtCore.QMetaObject.connectSlotsByName(dlMethod)

    def retranslateUi(self, dlMethod):
        _translate = QtCore.QCoreApplication.translate
        dlMethod.setWindowTitle(_translate("dlMethod", "Download Method Selection"))
        self.radioFirefox.setText(_translate("dlMethod", "Automatic - Firefox"))
        self.radioChrome.setText(_translate("dlMethod", "Automatic - Chrome"))
        self.label.setText(_translate("dlMethod", "How do you want to download DDLCv1.1.1? \n"
"(images-110.rpa will always download automatically if selected.)"))
        self.radioManual.setText(_translate("dlMethod", "Manual Download (New browser window/tab will open up)"))
        self.pushButton.setText(_translate("dlMethod", "Ok"))

        self.pushButton.clicked.connect(self.download)

        self.pushButton_2.setText(_translate("dlMethod", "Cancel"))


    def download(self):
        if self.radioManual.isChecked():
            print("Manual DL selected.")
            #Open ddlc.moe
            curOS = platform.system()
            if curOS == "Windows":
                os.system("start https://ddlc.moe")
            if curOS == "Linux":
                os.system("xdg-open https://ddlc.moe")
            if curOS == "Darwin":
                os.system("open https://ddlc.moe")
        else:
            if self.radioFirefox.isChecked():
                curBr = "Firefox"
            elif self.radioChrome.isChecked():
                curBr = "Chrome"
            config = configparser.ConfigParser(allow_no_value=True)
            config.read('config.ini')
            config['DEFAULT']['dlBrowser'] = curBr
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            import itchDownload



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlMethod = QtWidgets.QWidget()
    ui = Ui_dlMethod()
    ui.setupUi(dlMethod)
    dlMethod.show()
    sys.exit(app.exec_())

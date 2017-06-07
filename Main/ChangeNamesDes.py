# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangeNames.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChangeNames(object):
    def setupUi(self, ChangeNames):
        ChangeNames.setObjectName("ChangeNames")
        ChangeNames.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(ChangeNames)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(ChangeNames)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtFieldNameA = QtWidgets.QLineEdit(ChangeNames)
        self.txtFieldNameA.setObjectName("txtFieldNameA")
        self.gridLayout.addWidget(self.txtFieldNameA, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(ChangeNames)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtFieldNameB = QtWidgets.QLineEdit(ChangeNames)
        self.txtFieldNameB.setText("")
        self.txtFieldNameB.setObjectName("txtFieldNameB")
        self.gridLayout.addWidget(self.txtFieldNameB, 1, 1, 1, 1)
        self.btnSave = QtWidgets.QPushButton(ChangeNames)
        self.btnSave.setObjectName("btnSave")
        self.gridLayout.addWidget(self.btnSave, 2, 1, 1, 1)
        self.btnCancel = QtWidgets.QPushButton(ChangeNames)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 2, 0, 1, 1)

        self.retranslateUi(ChangeNames)
        QtCore.QMetaObject.connectSlotsByName(ChangeNames)

    def retranslateUi(self, ChangeNames):
        _translate = QtCore.QCoreApplication.translate
        ChangeNames.setWindowTitle(_translate("ChangeNames", "Change Names"))
        self.label_2.setText(_translate("ChangeNames", "Second Team Name"))
        self.label.setText(_translate("ChangeNames", "First Team Name"))
        self.btnSave.setText(_translate("ChangeNames", "Save"))
        self.btnCancel.setText(_translate("ChangeNames", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangeNames = QtWidgets.QWidget()
    ui = Ui_ChangeNames()
    ui.setupUi(ChangeNames)
    ChangeNames.show()
    sys.exit(app.exec_())


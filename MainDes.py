# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 378)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnUpB = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpB.setObjectName("btnUpB")
        self.gridLayout.addWidget(self.btnUpB, 2, 2, 1, 1)
        self.lblDash = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(72)
        self.lblDash.setFont(font)
        self.lblDash.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblDash.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDash.setObjectName("lblDash")
        self.gridLayout.addWidget(self.lblDash, 1, 1, 1, 1)
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setObjectName("btnReset")
        self.gridLayout.addWidget(self.btnReset, 2, 1, 1, 1)
        self.lblBScore = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(72)
        self.lblBScore.setFont(font)
        self.lblBScore.setObjectName("lblBScore")
        self.gridLayout.addWidget(self.lblBScore, 1, 2, 1, 1)
        self.btnDownB = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownB.setObjectName("btnDownB")
        self.gridLayout.addWidget(self.btnDownB, 3, 2, 1, 1)
        self.btnDownA = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownA.setObjectName("btnDownA")
        self.gridLayout.addWidget(self.btnDownA, 3, 0, 1, 1)
        self.lblAScore = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(72)
        self.lblAScore.setFont(font)
        self.lblAScore.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblAScore.setObjectName("lblAScore")
        self.gridLayout.addWidget(self.lblAScore, 1, 0, 1, 1)
        self.btnUpA = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpA.setObjectName("btnUpA")
        self.gridLayout.addWidget(self.btnUpA, 2, 0, 1, 1)
        self.lblAName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Khmer OS System")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lblAName.setFont(font)
        self.lblAName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblAName.setObjectName("lblAName")
        self.gridLayout.addWidget(self.lblAName, 0, 0, 1, 1)
        self.lblVS = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Khmer OS System")
        font.setPointSize(26)
        self.lblVS.setFont(font)
        self.lblVS.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVS.setObjectName("lblVS")
        self.gridLayout.addWidget(self.lblVS, 0, 1, 1, 1)
        self.lblBName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Khmer OS System")
        font.setPointSize(26)
        self.lblBName.setFont(font)
        self.lblBName.setObjectName("lblBName")
        self.gridLayout.addWidget(self.lblBName, 0, 2, 1, 1)
        self.btnChangeNames = QtWidgets.QPushButton(self.centralwidget)
        self.btnChangeNames.setObjectName("btnChangeNames")
        self.gridLayout.addWidget(self.btnChangeNames, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChangeTeams = QtWidgets.QAction(MainWindow)
        self.actionChangeTeams.setObjectName("actionChangeTeams")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scoreboard"))
        self.btnUpB.setText(_translate("MainWindow", "+TeamB+"))
        self.lblDash.setText(_translate("MainWindow", "-"))
        self.btnReset.setText(_translate("MainWindow", "Reset"))
        self.lblBScore.setText(_translate("MainWindow", "0"))
        self.btnDownB.setText(_translate("MainWindow", "-TeamB-"))
        self.btnDownA.setText(_translate("MainWindow", "-TeamA-"))
        self.lblAScore.setText(_translate("MainWindow", "0"))
        self.btnUpA.setText(_translate("MainWindow", "+TeamA+"))
        self.lblAName.setText(_translate("MainWindow", "Team A"))
        self.lblVS.setText(_translate("MainWindow", "VS"))
        self.lblBName.setText(_translate("MainWindow", "Team B"))
        self.btnChangeNames.setText(_translate("MainWindow", "Change Team Names"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionChangeTeams.setText(_translate("MainWindow", "Change Teams"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

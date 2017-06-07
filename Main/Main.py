import sys
#from PyQt5.QtCore import QCoreApplication, Qt
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from MainDes import Ui_MainWindow
import ChangeNamesDes

#Setup the app variables

#ui = MainDes.Ui_MainWindow()
#cn = ChangeNamesDes.Ui_ChangeNames()
#cnWindow = QtWidgets.QMainWindow()
#cn.setupUi(cnWindow)
#ui.setupUi(window)

aName = "Team A"
bName = "Team B"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    aScore = 0
    bScore = 0
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.cnWindow = None
        self.setupAll()

    #Increase team A's score
    def upA(self):
        self.aScore = self.aScore + 1
        self.showScore()

    #Increase team B's score
    def upB(self):
        self.bScore = self.bScore + 1
        self.showScore()

    #Decrease team A's score
    def downA(self):
        self.aScore = self.aScore - 1
        self.showScore()

    #Decrease team B's score
    def downB(self):
        self.bScore = self.bScore - 1
        self.showScore()

    #Resets everything to 0
    def reset(self):

        self.aScore = 0
        self.bScore = 0
        
        self.showScore()

    def showScore(self):

        self.lblAScore.setText("%d" % self.aScore)
        self.lblBScore.setText("%d" % self.bScore)

    def setNames(self):

        self.lblAName.setText(aName)
        self.lblBName.setText(bName)

    def setupAll(self):
        
        self.actionQuit.setShortcut("Ctrl+Q")
        
        self.btnUpA.clicked.connect(self.upA)
        self.btnUpB.clicked.connect(self.upB)

        self.btnDownA.clicked.connect(self.downA)
        self.btnDownB.clicked.connect(self.downB)

        self.btnReset.clicked.connect(self.reset)
        #self.btnChangeNames.clicked.connect(self.change_names)
        self.actionQuit.triggered.connect(self.close_application)

        self.setNames()

    #def change_names(self):
    #    self.cnWindow = ChangeWindow(self)
    #    self.cnWindow.show()

    def close_application(self):
        #Create a messagebox with options
                                    #Pass window instead of self to show on the window.    
        choice = QMessageBox.question(self, "Quit?", "Are you sure?", QMessageBox.Yes | QMessageBox.No)

        #What's the option picked?
        if choice == QMessageBox.Yes:
            #Close the app
            sys.exit()
        else:
            pass

#Launch it all!
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 360, 120))
        self.textEdit.setObjectName("textEdit")
        
        self.delayLabel = QtWidgets.QLabel(self.centralwidget)
        self.delayLabel.setGeometry(QtCore.QRect(20, 150, 60, 20))
        self.delayLabel.setObjectName("delayLabel")
        
        self.delaySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.delaySpinBox.setGeometry(QtCore.QRect(90, 150, 60, 20))
        self.delaySpinBox.setRange(0, 100)
        self.delaySpinBox.setObjectName("delaySpinBox")
        
        self.intervalLabel = QtWidgets.QLabel(self.centralwidget)
        self.intervalLabel.setGeometry(QtCore.QRect(20, 180, 60, 20))
        self.intervalLabel.setObjectName("intervalLabel")
        
        self.intervalSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.intervalSpinBox.setGeometry(QtCore.QRect(90, 180, 60, 20))
        self.intervalSpinBox.setRange(0.01, 10.0)
        self.intervalSpinBox.setSingleStep(0.01)
        self.intervalSpinBox.setObjectName("intervalSpinBox")
        
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(20, 220, 360, 40))
        self.startButton.setObjectName("startButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Typer"))
        self.delayLabel.setText(_translate("MainWindow", "Delay (s):"))
        self.intervalLabel.setText(_translate("MainWindow", "Interval (s):"))
        self.startButton.setText(_translate("MainWindow", "Start Typing"))


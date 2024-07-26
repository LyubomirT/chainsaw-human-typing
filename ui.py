from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 560, 340))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        
        self.settingsLayout = QtWidgets.QVBoxLayout()
        self.settingsLayout.setObjectName("settingsLayout")
        
        self.delayLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.delayLabel.setObjectName("delayLabel")
        self.settingsLayout.addWidget(self.delayLabel)
        
        self.delaySpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.delaySpinBox.setRange(0, 100)
        self.delaySpinBox.setObjectName("delaySpinBox")
        self.settingsLayout.addWidget(self.delaySpinBox)
        
        self.intervalLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.intervalLabel.setObjectName("intervalLabel")
        self.settingsLayout.addWidget(self.intervalLabel)
        
        self.intervalSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.intervalSpinBox.setRange(0.01, 10.0)
        self.intervalSpinBox.setSingleStep(0.01)
        self.intervalSpinBox.setObjectName("intervalSpinBox")
        self.settingsLayout.addWidget(self.intervalSpinBox)
        
        self.charPerStrokeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.charPerStrokeLabel.setObjectName("charPerStrokeLabel")
        self.settingsLayout.addWidget(self.charPerStrokeLabel)
        
        self.charPerStrokeSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.charPerStrokeSpinBox.setRange(1, 10)
        self.charPerStrokeSpinBox.setObjectName("charPerStrokeSpinBox")
        self.settingsLayout.addWidget(self.charPerStrokeSpinBox)
        
        self.enterCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.enterCheckBox.setObjectName("enterCheckBox")
        self.settingsLayout.addWidget(self.enterCheckBox)
        
        self.startButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.startButton.setObjectName("startButton")
        self.settingsLayout.addWidget(self.startButton)
        
        self.stopButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.stopButton.setEnabled(False)
        self.settingsLayout.addWidget(self.stopButton)
        
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar.setObjectName("progressBar")
        self.settingsLayout.addWidget(self.progressBar)
        
        self.horizontalLayout.addLayout(self.settingsLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Typer"))
        self.delayLabel.setText(_translate("MainWindow", "Delay (s):"))
        self.intervalLabel.setText(_translate("MainWindow", "Interval (s):"))
        self.charPerStrokeLabel.setText(_translate("MainWindow", "Chars per stroke:"))
        self.enterCheckBox.setText(_translate("MainWindow", "Type Enter"))
        self.startButton.setText(_translate("MainWindow", "Start Typing"))
        self.stopButton.setText(_translate("MainWindow", "Stop Typing"))

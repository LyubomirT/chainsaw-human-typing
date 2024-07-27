from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes
import json
import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        MainWindow.setMaximumSize(QtCore.QSize(600, 500))
        MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
        if sys.platform == "win32" and hasattr(ctypes.windll, "shell32"):
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Chainsaw Human Typing")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 561, 421))
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
        self.intervalSpinBox.setRange(0.00001, 10.0)
        self.intervalSpinBox.setSingleStep(0.00001)
        self.intervalSpinBox.setDecimals(5)
        self.intervalSpinBox.setObjectName("intervalSpinBox")
        self.settingsLayout.addWidget(self.intervalSpinBox)
        
        self.charPerStrokeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.charPerStrokeLabel.setObjectName("charPerStrokeLabel")
        self.settingsLayout.addWidget(self.charPerStrokeLabel)
        
        self.charPerStrokeSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.charPerStrokeSpinBox.setRange(1, 50)
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
        
        self.languageComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.languageComboBox.setObjectName("languageComboBox")
        self.settingsLayout.addWidget(self.languageComboBox)

        self.lightModeCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.lightModeCheckBox.setObjectName("lightModeCheckBox")
        self.settingsLayout.addWidget(self.lightModeCheckBox)
        
        self.horizontalLayout.addLayout(self.settingsLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        self.current_language = "English"  # Default language
        self.translations = {}
        self.load_translations()
        
        self.languageComboBox.currentTextChanged.connect(self.change_language)
        self.update_ui_text()

    def load_translations(self):
        translations_dir = "translations"
        for filename in os.listdir(translations_dir):
            if filename.endswith(".json"):
                language_code = filename[:-5]  # Remove .json extension
                with open(os.path.join(translations_dir, filename), "r", encoding="utf-8") as f:
                    self.translations[language_code] = json.load(f)
                self.languageComboBox.addItem(language_code)

    def change_language(self, language):
        self.current_language = language
        self.update_ui_text()

    def update_ui_text(self):
        translation = self.translations.get(self.current_language, self.translations["English"])
        for item in translation["MainWindow"]:
            component = getattr(self, item["component"], None)
            if component:
                component.setText(item["text"])
        
        _translate = QtCore.QCoreApplication.translate
        self.delayLabel.setText(_translate("MainWindow", "Delay (seconds)"))
        self.intervalLabel.setText(_translate("MainWindow", "Interval (seconds)"))
        self.charPerStrokeLabel.setText(_translate("MainWindow", "Characters per stroke"))
        self.enterCheckBox.setText(_translate("MainWindow", "Type Enter"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.lightModeCheckBox.setText(_translate("MainWindow", "Light Mode"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
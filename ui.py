from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes
import json
import os
import sys

class Ui_MainWindow(object):
    def __init__(self):
        if os.path.exists("language.txt"):
            with open("language.txt", "r", encoding="utf-8") as f:
                self.current_language = f.read()
        else: 
            self.current_language = "English"
        self.translations = {}

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
        self.languageComboBox.currentTextChanged.connect(lambda hakka: self.change_language)
        self.settingsLayout.addWidget(self.languageComboBox)

        self.lightModeCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.lightModeCheckBox.setObjectName("lightModeCheckBox")
        self.lightModeCheckBox.clicked.connect(self.toggleTheme)
        self.lightModeCheckBox.setChecked(True)
        self.settingsLayout.addWidget(self.lightModeCheckBox)
        
        self.horizontalLayout.addLayout(self.settingsLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load_translations()

        self.update_ui_text()

        self.load_theme_based_on_last_choice()

        # set the current language of the dropdown to the saved language
        self.languageComboBox.setCurrentText(self.current_language)

    def load_translations(self):
        self.translations = {}
        translations_dir = "translations"
        for filename in os.listdir(translations_dir):
            if filename.endswith(".json"):
                language_code = filename[:-5]  # Remove .json extension
                with open(os.path.join(translations_dir, filename), "r", encoding="utf-8") as f:
                    self.translations[language_code] = json.load(f)
                self.languageComboBox.addItem(language_code)
    
    def load_theme_based_on_last_choice(self):
        if not os.path.exists("theme.txt"):
            return
        with open("theme.txt", "r", encoding="utf-8") as f:
            theme = f.read()
        if theme == "dark":
            self.lightModeCheckBox.setChecked(False)
            self.toggleTheme()
        if theme == "light":
            self.lightModeCheckBox.setChecked(True)
            self.toggleTheme()

    def change_language(self):
        self.current_language = self.languageComboBox.currentText()
        print(f"Changed language to {self.current_language}")
        with open("language.txt", "w", encoding="utf-8") as f:
            f.write(self.current_language)
        self.update_ui_text()


    def update_ui_text(self):
        translation = self.translations.get(self.current_language, self.translations["English"])
        for item in translation["MainWindow"]:
            component = getattr(self, item["component"], None)
            if component:
                component.setText(item["text"])
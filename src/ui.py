from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes
import json
import os
import sys

class PlainTextEdit(QtWidgets.QTextEdit):
    def insertFromMimeData(self, source):
        if source.hasText():
            self.insertPlainText(source.text())

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
        MainWindow.resize(800, 600)  # Increased width to accommodate presets
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        MainWindow.setMaximumSize(QtCore.QSize(800, 700))
        MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
        if sys.platform == "win32" and hasattr(ctypes.windll, "shell32"):
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Chainsaw Human Typing")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 681))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        
        self.mainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        
        # Left Side Layout (TextEdit and Settings)
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.leftLayout.setObjectName("leftLayout")
        
        self.textEdit = PlainTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setAcceptRichText(False)
        self.leftLayout.addWidget(self.textEdit)
        
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

        self.mistakePercentageLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.mistakePercentageLabel.setObjectName("mistakePercentageLabel")
        self.settingsLayout.addWidget(self.mistakePercentageLabel)

        self.mistakePercentageSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.mistakePercentageSpinBox.setRange(0, 100)
        self.mistakePercentageSpinBox.setObjectName("mistakePercentageSpinBox")
        self.settingsLayout.addWidget(self.mistakePercentageSpinBox)

        self.randomizeIntervalCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.randomizeIntervalCheckBox.setObjectName("randomizeIntervalCheckBox")
        self.settingsLayout.addWidget(self.randomizeIntervalCheckBox)
        
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
        
        self.leftLayout.addLayout(self.settingsLayout)
        self.mainLayout.addLayout(self.leftLayout, 3)
        
        # Right Side Layout (Presets)
        self.presetsLayout = QtWidgets.QVBoxLayout()
        self.presetsLayout.setObjectName("presetsLayout")
        
        self.savePresetButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.savePresetButton.setObjectName("savePresetButton")
        self.presetsLayout.addWidget(self.savePresetButton)
        
        self.presetsList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.presetsList.setObjectName("presetsList")
        self.presetsLayout.addWidget(self.presetsList)
        
        self.renamePresetButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.renamePresetButton.setObjectName("renamePresetButton")
        self.presetsLayout.addWidget(self.renamePresetButton)
        
        self.deletePresetButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deletePresetButton.setObjectName("deletePresetButton")
        self.presetsLayout.addWidget(self.deletePresetButton)
        
        self.mainLayout.addLayout(self.presetsLayout, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load_translations()

        self.update_ui_text()

        self.load_theme_based_on_last_choice()

    def load_translations(self):
        self.translations = {}
        translations_dir = "translations"
        if not os.path.exists(translations_dir):
            os.makedirs(translations_dir)
        for filename in os.listdir(translations_dir):
            if filename.endswith(".json"):
                language_code = filename[:-5]  # Remove .json extension
                with open(os.path.join(translations_dir, filename), "r", encoding="utf-8") as f:
                    self.translations[language_code] = json.load(f)
                    language_original = self.translations[language_code].get("original", "Unknown")
                self.languageComboBox.addItem(language_code + " - " + language_original)
                if language_code == self.current_language:
                    self.current_language = language_code
                    self.languageComboBox.setCurrentText(self.current_language + " - " + language_original)
    
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
        self.current_language = self.languageComboBox.currentText().split(" - ")[0]
        print(f"Changed language to {self.current_language}")
        with open("language.txt", "w", encoding="utf-8") as f:
            f.write(self.current_language)
        self.update_ui_text()

    def update_ui_text(self):
        translation = self.translations.get(self.current_language, self.translations.get("English", {}))
        if not translation:
            return
        for item in translation.get("MainWindow", []):
            component = getattr(self, item["component"], None)
            if component:
                component.setText(item["text"])

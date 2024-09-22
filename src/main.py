import sys
import time
import random
import string
import json
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QInputDialog
from ui import Ui_MainWindow
from pynput.keyboard import Controller, Key

class TypingThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self, text, interval, type_enter, chars_per_stroke, randomize_interval, mistake_percentage):
        super().__init__()
        self.text = text
        self.interval = interval
        self.type_enter = type_enter
        self.chars_per_stroke = chars_per_stroke
        self.randomize_interval = randomize_interval
        self.mistake_percentage = mistake_percentage
        self.running = True
        self.keyboard = Controller()
        print(f"TypingThread initialized with randomize_interval: {self.randomize_interval}")  # Debug print

    def run(self):
        i = 0
        while i < len(self.text) and self.running:
            if self.text[i] == '\n' and self.type_enter:
                self.keyboard.press(Key.enter)
                self.keyboard.release(Key.enter)
                i += 1
            else:
                chunk = self.text[i:i + self.chars_per_stroke]
                self.type_with_mistake(chunk)
                i += self.chars_per_stroke
            
            if self.randomize_interval:
                current_interval = self.interval * random.uniform(0.1, 3)
                print(f"Randomized interval: {current_interval}")  # Debug print
            else:
                current_interval = self.interval
                print(f"Fixed interval: {current_interval}")  # Debug print
            
            time.sleep(current_interval)
            self.progress.emit(int(i / len(self.text) * 100))
        self.finished.emit()

    def type_with_mistake(self, chunk):
        for char in chunk:
            if random.random() < self.mistake_percentage / 100:
                # Make a typo
                wrong_char = random.choice(string.ascii_lowercase)
                self.keyboard.type(wrong_char)
                time.sleep(self.interval * 2)  # Pause after typo
                
                # Type a few more characters
                extra_chars = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 3)))
                self.keyboard.type(extra_chars)
                time.sleep(self.interval * 3)  # Pause after extra chars
                
                # Backspace to correct the mistake
                for _ in range(len(extra_chars) + 1):
                    self.keyboard.press(Key.backspace)
                    self.keyboard.release(Key.backspace)
                    time.sleep(self.interval * 0.5)
                
                # Type the correct character
                self.keyboard.type(char)
            else:
                # Type normally
                self.keyboard.type(char)
            time.sleep(self.interval)

    def stop(self):
        self.running = False

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Chainsaw Human Typing")
        self.startButton.clicked.connect(self.start_typing)
        self.stopButton.clicked.connect(self.stop_typing)
        self.languageComboBox.currentTextChanged.connect(self.change_language)
        self.lightModeCheckBox.toggled.connect(self.toggleTheme)
        
        # Presets Buttons
        self.savePresetButton.clicked.connect(self.save_preset)
        self.renamePresetButton.clicked.connect(self.rename_preset)
        self.deletePresetButton.clicked.connect(self.delete_preset)
        self.presetsList.itemDoubleClicked.connect(self.load_preset)

        self.thread = None
        self.presets = {}
        self.presets_file = "presets.json"
        self.load_presets()

    def start_typing(self):
        text = self.textEdit.toPlainText()
        try:
            delay = int(self.delaySpinBox.value())
            interval = float(self.intervalSpinBox.value())
            type_enter = self.enterCheckBox.isChecked()
            chars_per_stroke = int(self.charPerStrokeSpinBox.value())
            randomize_interval = self.randomizeIntervalCheckBox.isChecked()
            mistake_percentage = int(self.mistakePercentageSpinBox.value())
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid input for delay, interval, chars per stroke, or mistake percentage.")
            return

        print(f"Starting typing with randomize_interval: {randomize_interval}")  # Debug print

        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        if delay > 0:
            QTimer.singleShot(delay * 1000, lambda: self.initiate_typing(text, interval, type_enter, chars_per_stroke, randomize_interval, mistake_percentage))
        else:
            self.initiate_typing(text, interval, type_enter, chars_per_stroke, randomize_interval, mistake_percentage)

    def initiate_typing(self, text, interval, type_enter, chars_per_stroke, randomize_interval, mistake_percentage):
        self.thread = TypingThread(text, interval, type_enter, chars_per_stroke, randomize_interval, mistake_percentage)
        self.thread.progress.connect(self.update_progress)
        self.thread.finished.connect(self.typing_finished)
        self.progressBar.setValue(0)
        self.thread.start()

    def update_progress(self, value):
        self.progressBar.setValue(value)
    
    def typing_finished(self):
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)

    def stop_typing(self):
        if self.thread:
            self.thread.stop()
            self.thread.wait()
            self.thread = None
        self.typing_finished()

    def toggleTheme(self):
        if self.lightModeCheckBox.isChecked():
            self.setStyleSheet(open("style.css").read())
        else:
            self.setStyleSheet(open("darkmode.css").read())
        self.save_theme_based_on_last_choice()

    def save_theme_based_on_last_choice(self):
        with open("theme.txt", "w", encoding="utf-8") as f:
            f.write("light" if self.lightModeCheckBox.isChecked() else "dark")
    
    # Presets Methods
    def load_presets(self):
        if os.path.exists(self.presets_file):
            try:
                with open(self.presets_file, "r", encoding="utf-8") as f:
                    self.presets = json.load(f)
                for preset_name in self.presets:
                    self.presetsList.addItem(preset_name)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load presets: {e}")
        else:
            self.presets = {}

    def save_presets_to_file(self):
        try:
            with open(self.presets_file, "w", encoding="utf-8") as f:
                json.dump(self.presets, f, indent=4)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save presets: {e}")

    def save_preset(self):
        preset_name, ok = self.get_text_input("Save Preset", "Enter a name for the preset:")
        if ok and preset_name:
            if preset_name in self.presets:
                QMessageBox.warning(self, "Warning", "A preset with this name already exists.")
                return
            self.presets[preset_name] = self.current_settings()
            self.presetsList.addItem(preset_name)
            self.save_presets_to_file()
            QMessageBox.information(self, "Success", f"Preset '{preset_name}' saved successfully.")

    def rename_preset(self):
        selected_item = self.presetsList.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Warning", "Please select a preset to rename.")
            return
        old_name = selected_item.text()
        new_name, ok = self.get_text_input("Rename Preset", "Enter a new name for the preset:", old_name)
        if ok and new_name:
            if new_name in self.presets:
                QMessageBox.warning(self, "Warning", "A preset with this name already exists.")
                return
            self.presets[new_name] = self.presets.pop(old_name)
            selected_item.setText(new_name)
            self.save_presets_to_file()
            QMessageBox.information(self, "Success", f"Preset renamed to '{new_name}' successfully.")

    def delete_preset(self):
        selected_item = self.presetsList.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Warning", "Please select a preset to delete.")
            return
        preset_name = selected_item.text()
        confirm = QMessageBox.question(self, "Confirm Delete", f"Are you sure you want to delete preset '{preset_name}'?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.presets.pop(preset_name, None)
            self.presetsList.takeItem(self.presetsList.row(selected_item))
            self.save_presets_to_file()
            QMessageBox.information(self, "Success", f"Preset '{preset_name}' deleted successfully.")

    def load_preset(self, item):
        preset_name = item.text()
        settings = self.presets.get(preset_name)
        if settings:
            self.apply_settings(settings)
            QMessageBox.information(self, "Preset Loaded", f"Preset '{preset_name}' has been loaded.")
        else:
            QMessageBox.warning(self, "Warning", f"Preset '{preset_name}' not found.")

    def current_settings(self):
        return {
            "delay": self.delaySpinBox.value(),
            "interval": self.intervalSpinBox.value(),
            "type_enter": self.enterCheckBox.isChecked(),
            "chars_per_stroke": self.charPerStrokeSpinBox.value(),
            "randomize_interval": self.randomizeIntervalCheckBox.isChecked(),
            "mistake_percentage": self.mistakePercentageSpinBox.value(),
            "light_mode": self.lightModeCheckBox.isChecked(),
            "language": self.current_language
        }

    def apply_settings(self, settings):
        self.delaySpinBox.setValue(settings.get("delay", 0))
        self.intervalSpinBox.setValue(settings.get("interval", 0.0))
        self.enterCheckBox.setChecked(settings.get("type_enter", False))
        self.charPerStrokeSpinBox.setValue(settings.get("chars_per_stroke", 1))
        self.randomizeIntervalCheckBox.setChecked(settings.get("randomize_interval", False))
        self.mistakePercentageSpinBox.setValue(settings.get("mistake_percentage", 0))
        self.lightModeCheckBox.setChecked(settings.get("light_mode", True))
        self.toggleTheme()
        language = settings.get("language", "English")
        index = self.languageComboBox.findText(language + " - " + self.translations.get(language, {}).get("original", "Unknown"))
        if index != -1:
            self.languageComboBox.setCurrentIndex(index)

    def get_text_input(self, title, label, default_text=""):
        text, ok = QInputDialog.getText(self, title, label, text=default_text)
        return text, ok

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if os.path.exists("theme.txt"):
        with open("theme.txt", "r", encoding="utf-8") as f:
            theme = f.read()
        if theme == "light":
            app.setStyleSheet(open("style.css").read())
        else:
            app.setStyleSheet(open("darkmode.css").read())
    else:
        app.setStyleSheet(open("style.css").read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

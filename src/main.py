import sys
import time
import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal
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
        self.thread = None

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
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("style.css").read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
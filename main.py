import sys
import time
import pyautogui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, Qt
from ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.start_typing)
    
    def start_typing(self):
        text = self.textEdit.toPlainText()
        delay = int(self.delaySpinBox.value())
        interval = float(self.intervalSpinBox.value())
        
        QTimer.singleShot(delay * 1000, lambda: self.type_text(text, interval))
    
    def type_text(self, text, interval):
        for char in text:
            pyautogui.typewrite(char)
            time.sleep(interval)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("style.css").read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

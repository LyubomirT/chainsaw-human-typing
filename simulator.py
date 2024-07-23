import pyautogui
import time

def type_text(text, interval):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(interval)

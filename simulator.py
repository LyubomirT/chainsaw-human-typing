import pyautogui
import time

def type_text(text, interval, type_enter=True, chars_per_stroke=1):
    i = 0
    while i < len(text):
        if text[i] == '\n' and type_enter:
            pyautogui.press('enter')
            i += 1
        else:
            pyautogui.write(text[i:i + chars_per_stroke])
            i += chars_per_stroke
        time.sleep(interval)

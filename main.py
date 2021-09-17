import pyautogui
import keyboard
import time

x, y= pyautogui.size()
x /= 2 
y /= 2
while True:
    if keyboard.is_pressed('q'):
        try:
            pyautogui.moveTo(x, y, duration = 0)
        except:
            print('error')
    else:
        time.sleep(.1)
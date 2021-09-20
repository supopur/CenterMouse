W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green

def center():
    #gets display ressolution
    x, y= pyautogui.size()
    x /= 2 
    y /= 2
    
    while True:
        if keyboard.is_pressed('q'):
            try:
                #moves the mouse to the center of the screen
                #the duration value means how fast will the mouse get to the center
                pyautogui.moveTo(x, y, duration = 0)
            except:
                print('error')

        else: #if you wanna fix the script sometimes not registering key presses remove this line
            time.sleep(.1) #and this line too
            
try:
    import pyautogui
    import keyboard
    import time
except:
    print(R+'ERROR IMPORTING MODULES'+W)
else:
    print(G+'No exception occured'+W)
    center()
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green

def center():
    #gets display ressolution
    x, y= pyautogui.size()
    x /= 2 
    y /= 2

    def more_center():
        print('the more_center function was called')
        if keyboard.is_pressed('q'):
            try:
                #moves the mouse to the center of the screen
                #the duration value means how fast will the mouse get to the center
                pyautogui.moveTo(x, y, duration = 0)
            except:
                print('error')
        time.sleep(.1)
        ws.after(0, more_center)
        
    
    ws = Tk()
    ws.title('Mouse center')
    def stop():
        ws.destroy()
        sys.exit(W+'Successfully stopped'+W)
    Button(ws, text="Stop", command=stop).pack(pady=20)
    ws.update()
    ws.after(0, more_center)
    ws.mainloop()
    

            
            
try:
    import pyautogui
    import keyboard
    import time
    from tkinter import *
    import sys
    
except:
    print(R+'ERROR IMPORTING MODULES'+W)
else:
    print(G+'No exception occured'+W)
    center()
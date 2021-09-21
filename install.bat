@echo off
echo don't worry about errors
pip install pyautogui
pip install keyboard
pip install time
pip install tkinter
pip install sys
echo if you saw any errors don't panic
echo Do you want to launch the script? (y/n)
set /p Input=Enter Yes or No:
If /I "%Input%"=="y" goto yes
goto no
:yes
python main.py
:no
pause
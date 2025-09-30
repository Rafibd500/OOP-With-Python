# N:B: code run kore 3 sec er moddhe code er niche othoba any text editor e mouse left click korle sekhane pattern dekha jabe 
import pyautogui
import time
n = int(input())
time.sleep(3)
x = f'{n}\n'
pyautogui.write(x, interval=".01")
for i in range(1, n+1):
    for j in range(1, i+1):
        pyautogui.write('#', interval=".01")
    pyautogui.press("enter")
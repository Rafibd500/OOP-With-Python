import pyautogui
from time import sleep
a, b = pyautogui.size()
print(a, b)
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)
# pyautogui.moveTo(100, 100)
# pyautogui.click()
# pyautogui.click(100, 100)
# pyautogui.click('button.png')     ### Confusion

# list = ['Rahim', 'Karim', 'Babul', 'Kabul', 'Kodu']
# sleep(5)
# for i in range (0,10):
#     pyautogui.write(list[i%4], interval=0.01)
#     pyautogui.press('enter')
pyautogui.FAILSAFE = False

sleep(5)
for i in range(0, 10):
    sleep(0.5)
    # currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click()
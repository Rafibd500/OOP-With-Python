import pyautogui
from time import sleep
a, b = pyautogui.size()
print(a, b)
currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)
# pyautogui.moveTo(100, 100)
# pyautogui.click()
# pyautogui.click(100, 100)
# pyautogui.click('button.png')     ### Confusion

list = ['Rahim', 'Karim', 'Babul', 'Kabul', 'Kodu']
names = [
    "Rahim", "Karim", "Babul", "Kabul", "Kodu", 
    "Jamil", "Shakil", "Hasib", "Noman", "Ratan",
    "Sajib", "Farid", "Nasim", "Kabir", "Asif",
    "Anis", "Robin", "Shahin", "Arif", "Nayeem",
    "Sohag", "Milon", "Biplob", "Rasel", "Tareq",
    "Imran", "Shuvo", "Amin", "Ripon", "Sajibul",
    "Mamun", "Fahim", "Parvez", "Sohan", "Hridoy",
    "Shanto", "Badol", "Liton", "Rony", "Joy",
    "Monir", "Javed", "Rafiq", "Selim", "Rubel",
    "Sadiq", "Nafis", "Arafat", "Tuhin", "Kamal"
]

# sleep(5)
# for i in range (0,20):
#     x = len(list) - 1
#     pyautogui.write(list[i%4], interval=0.01)
#     pyautogui.press('enter')
sleep(5)
for name in names:
    pyautogui.write(name, interval=0.001)
    pyautogui.press('enter')


# pyautogui.FAILSAFE = False

# sleep(5)
# for i in range(0, 20):
#     sleep(1)
#     # currentMouseX, currentMouseY = pyautogui.position()
#     # pyautogui.click(1869, 648)
#     # pyautogui.press('down')
#     pyautogui.scroll(-300)

# print(currentMouseX, currentMouseY)

import pyautogui as pt #pip install pyautogui
import time #pip install time

limit = input("enter limit:")
message = input("enter message:")
i = 0

time.sleep(3)

while i<int(limit):
    pt.typewrite(message)
    pt.press("enter")

    i+=1
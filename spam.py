import pyautogui as py
import time

py.moveTo(913,703)
c = int(input("How many times do you want to do?\t"))
total = 0
while True:
    time.sleep(1)
    py.click()
    total += 1
    if c == 1:
        break 
    c -= 1
print(total)
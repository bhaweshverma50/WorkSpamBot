import pyautogui
import time

# ****** For spamming from text file, add you script in the script.txt file and uncomment the while loop below and comment the other one *******

# while(True):
#     time.sleep(10)
#     file = open("script.txt", "r")
#     for msg in file:
#         pyautogui.typewrite(msg)
#         pyautogui.press("enter")
#     file.close()


# ******* This while is for casino bot of discord which will automatically work after the set time interval (here i have set 30 as on my server its 30 seconds) *******

interval = 35
word = ".work"

while(True):
    time.sleep(interval)
    pyautogui.typewrite(word)
    pyautogui.press("enter")

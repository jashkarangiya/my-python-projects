import pyautogui, time
time.sleep(20)

i = 0

for i in range(100):
    read = open("word", 'r')
    for words in read:
        pyautogui.typewrite(words)
        pyautogui.press("enter")




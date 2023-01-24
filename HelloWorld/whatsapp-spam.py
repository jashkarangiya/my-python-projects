import pyautogui, time
time.sleep(10)

i = 0

for i in range(10):
    read = open("word", 'r')
    for words in read:
        pyautogui.typewrite(words)
        pyautogui.press("enter")

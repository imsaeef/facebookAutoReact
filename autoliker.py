import pyautogui
import time
pyautogui.FAILSAFE = False
# like for 5 post react
for i in range(0, 5):
    time.sleep(3)
    # command 
    pyautogui.press('j') # j for scrolling
    time.sleep(3)
    pyautogui.press('l') # l for like
    # time.sleep(1)
    # pyautogui.press(['right']) # right key for 'love' react
    # pyautogui.press(['right','right']) # right key for 'care' react
    # pyautogui.press(['right','right','right']) # right key for 'haha' react
    # pyautogui.press(['right','right','right','right'])  # right key for 'wow' react
    # pyautogui.press(['right','right','right','right','right']) # right key for 'sad' react
    # pyautogui.press(['right','right','right','right','right','right']) # right key for 'angry' react
    time.sleep(1)
    pyautogui.press('enter') # enter for sel react

import pyautogui
import Constants
import time

def locate(s):
    acc = 0
    while True:
         acc = acc + 1
         if (acc > 3):
            return 0
         im1 = pyautogui.screenshot()
         coord = pyautogui.locateOnScreen(Constants.ImagePath + s, confidence = 0.8)
         if (coord is not None):
            buttonpoint = pyautogui.center(coord)
            x, y = buttonpoint
            time.sleep(0.5)
            print(x,y)
            return 1
        
def getXYCoord(s):
    acc = 0
    while True:
         acc = acc + 1
         if (acc > 3):
            return -999, -999
         im1 = pyautogui.screenshot()
         coord = pyautogui.locateOnScreen(Constants.ImagePathENG + s, confidence = 0.8)
         if (coord is not None):
            buttonpoint = pyautogui.center(coord)
            x, y = buttonpoint
            time.sleep(0.5)
            return x, y

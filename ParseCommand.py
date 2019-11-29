import pyautogui
import time
import Cursor
import Recognition
import Start

def SendMouseClick(a):
    x, y = Recognition.getXYCoord(a)
    print(x,y)
    if (x != -999 & y != -999):
        Cursor.MoveCursor(x,y)
        pyautogui.click(x,y)
        time.sleep(0.5)
        
def SendKeyInput(a, b):
    if (Recognition.locate(a)) == 1:
        pyautogui.press(b)

def TerminateKeyInput(a, b, c):
    if (Recognition.locate(a)) == 1:
        pyautogui.press(b)
        return c
    else: 
        return ""

def parse(str):
    #start up the emulator
    if (str == "-init"):
        Start.start()
        Done = TerminateKeyInput("icon.png", "enter", "App opened.")
        if (Done != ""): return Done
        else: return "Error starting up the app."
        
    #return to home
    if (str == "-h"):
        Start.openApp()
        SendKeyInput("home.png", "h")

    #run dimension missions
    if (str == "-dm"):
        Start.openApp()
        SendMouseClick("home.png")
        SendMouseClick("enter.png")
        SendMouseClick("dm.png")
        SendMouseClick("ready.png")
        SendMouseClick("clear.png")
        SendMouseClick("cmax.png")
        SendMouseClick("home.png")

        noEnergyErr = TerminateKeyInput("noenergy.png", "n", "Out of energy. Returning to home.")
        if noEnergyErr != "":
            SendKeyInput("home.png", "h")
            return noEnergyErr          
        time.sleep(4)
        SendMouseClick("close.png")
        Done = TerminateKeyInput("home.png", "h", "Done.")
        if Done != "":
            return "Done."
        else: return "Error."

    #collect antimatter from store
    if (str == "-lab col"):
        Start.openApp()
        SendMouseClick("home.png")
        SendMouseClick("list.png")
        SendMouseClick("lab.png")
        SendMouseClick("amcollect.png")
        time.sleep(0.5)
        Done = TerminateKeyInput("home.png", "h", "Antimatter collected. Returning to home.")
        if Done != "":
            return Done
        else:
            return "An error occurred."
    
    #Legendary battle: Loki Ragnarok 
    if (str == "-lb"):
        Start.openApp()
        SendMouseClick("start.png")
        pyautogui.press("l")
        time.sleep(10)
        pyautogui.press("l")
        while True:
            if (Recognition.locate("repeat.png")):
                pyautogui.press("l")
                time.sleep(4)
                return "Stage complete."
            pyautogui.press("l")
            pyautogui.press("l")
            time.sleep(0.5)
            pyautogui.press(";")
            pyautogui.press(";")
            time.sleep(0.5)
            pyautogui.press("'")
            pyautogui.press("'")
            time.sleep(0.5)
            pyautogui.press("[")
            pyautogui.press("[")
            time.sleep(0.5)
            pyautogui.press("p")
            pyautogui.press("p")
            time.sleep(0.5)

    return ""


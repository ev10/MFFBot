import pyautogui
import Recognition
import time

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
    #return to home
    if (str == "-h"):
        SendKeyInput("home.png", "h")

    #run dimension missions
    if (str == "-dm"):
        SendKeyInput("home.png", "h")
        SendKeyInput("enter.png", "e")
        SendKeyInput("dm.png", "n")
        SendKeyInput("ready.png", "r")
        SendKeyInput("clear.png", "r")
        SendKeyInput("cmax.png", "n")
        noEnergyErr = TerminateKeyInput("noenergy.png", "n", "Out of energy. Returning to home.")
        if noEnergyErr != "":
            SendKeyInput("home.png", "h")
            return noEnergyErr          
        time.sleep(1)
        SendKeyInput("close.png", "k")
        SendKeyInput("home.png", "h")
        return "Done."

    #collect antimatter from store
    if (str == "-lab col"):
        SendKeyInput("home.png", "h")
        SendKeyInput("list.png", "c")
        SendKeyInput("lab.png", "1")
        SendKeyInput("amcollect.png", "k")
        Done = TerminateKeyInput("home.png", "h", "Antimatter collected. Returning to home.")
        if Done != "":
            return Done
        else:
            return "An error occurred."

    return ""


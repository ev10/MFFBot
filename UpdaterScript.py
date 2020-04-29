import PIL
from PIL import Image
from PIL import ImageOps
from pytesseract import *
import numpy as np
import pyautogui
import time

#img_dir=str(input())

def extract (img_path):
    pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" #INSTALL TESSERACT OCR ENGINE
    img_file = img_path
    im = Image.open(img_file).convert("L") #CONVERT TO GRAYSCALE
    inverted_image = PIL.ImageOps.invert(im)
    im=inverted_image
    text = image_to_string(im)
    return text

namecoord = (1472, 380, 131, 20) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
idcoord = (1472, 425, 131, 20) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
yearcoord = (1472, 470, 131, 20) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
countcoord = (1472, 510, 131, 20) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
setcoord = (1472, 600, 131, 20) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
termcoord = (1472, 645, 131, 20) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
socoord = (1477, 280, 100, 20) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
rcoord = (1702, 280, 100, 20) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS

def screengrab():
    time.sleep(0.3)
    pyautogui.screenshot("card1.jpg", region = namecoord)
    pyautogui.screenshot("card2.jpg", region = idcoord)
    pyautogui.screenshot("card3.jpg", region = yearcoord)
    pyautogui.screenshot("card4.jpg", region = countcoord)
    pyautogui.screenshot("card5.jpg", region = setcoord)
    pyautogui.screenshot("card6.jpg", region = termcoord)
    pyautogui.screenshot("card7.jpg", region = socoord)
    pyautogui.screenshot("card8.jpg", region = rcoord)

cardTotal = 4626

acc = 1

for acc in range(1,15):
    screengrab()
    name = extract(r"C:\Users\ev\source\repos\tmcscraper\tmcscraper\card1.jpg") #THIS IS THE DIRECTORY USED TO STORE TEMP FILES
    id = extract(r"C:\Users\ev\source\repos\tmcscraper\tmcscraper\card2.jpg") #THIS IS THE DIRECTORY USED TO STORE TEMP FILES
    year = extract(r"C:\Users\ev\source\repos\tmcscraper\tmcscraper\card3.jpg") #THIS IS THE DIRECTORY USED TO STORE TEMP FILES
    cc = extract(r"C:\Users\ev\source\repos\tmcscraper\tmcscraper\card4.jpg") #THIS IS THE DIRECTORY USED TO STORE TEMP FILES
    set = extract(r"C:\Users\ev\source\repos\tmcscraper\tmcscraper\card5.jpg") #THIS IS THE DIRECTORY USED TO STORE TEMP FILES
    term = extract(r"C:\Users\ev\source\repos\tmcscraper\tmcscraper\card6.jpg") #THIS IS THE DIRECTORY USED TO STORE TEMP FILES
    so = extract(r"C:\Users\ev\source\repos\tmcscraper\tmcscraper\card7.jpg") #THIS IS THE DIRECTORY USED TO STORE TEMP FILES
    r = extract(r"C:\Users\ev\source\repos\tmcscraper\tmcscraper\card8.jpg") #THIS IS THE DIRECTORY USED TO STORE TEMP FILES
    filename = "m" + str(cardTotal) + ".jpg"
    year.replace('+','')
    if ("OUT" in so):
        so = "Y"
    else:
        so = "N"

    pyautogui.click(1475, 740) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
    time.sleep(0.5)
    pyautogui.screenshot(str(filename), region = (1400, 150, 420, 580)) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
    pyautogui.click(1608, 800) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
    pyautogui.moveTo(1719, 534) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
    pyautogui.dragTo(1221, 534, 0.7, button='left') #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
    time.sleep(0.3)
    if (so == "Y"):
        print(name + delim + id + delim + year + delim + cc + delim + set + delim + term + delim + so + delim + r)
    else:
        print(name + delim + id + delim + year + delim + cc + delim + set + delim + so + delim + r)
    pyautogui.click(1747, 742) #COORDINATES MAY VARY, USE QUERYMOUSEPOSITION TO UPDATE COORDS
    cardTotal = cardTotal + 1

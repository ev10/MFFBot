import time
from PIL import Image
from PIL import ImageOps
from pytesseract import *
import numpy as np
import mss

import Keystroke
import Constants

pytesseract.tesseract_cmd = Constants.TesseractPath

def RealTimeOcr():
    with mss.mss() as sct:
        while True:
            im = np.asarray(sct.grab(Constants.ScreenCapRange))
            text = pytesseract.image_to_string(im)
            print(text)
            time.sleep(Constants.SCTimeDelay)


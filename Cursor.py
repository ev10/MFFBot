import pyautogui
import random
import scipy
import time
from scipy import interpolate
import Constants

def MoveCursor(xDest,yDest):
    cp = random.randint(3, 5)
    x1, y1 = pyautogui.position()  # Starting position
    x2, y2 = int(xDest), int(yDest) # Destination

    # Distribute control points
    x = scipy.linspace(x1, x2, num=cp, dtype='int')
    y = scipy.linspace(y1, y2, num=cp, dtype='int')

    # Randomize coordinates along path
    RND = 10
    xr = scipy.random.randint(-RND, RND, size=cp)
    yr = scipy.random.randint(-RND, RND, size=cp)
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    # Bezier curve approximation
    degree = 3 if cp > 3 else cp - 1 

    tck, u = scipy.interpolate.splprep([x, y], k=degree)
    u = scipy.linspace(0, 1, num=max(pyautogui.size()))
    points = scipy.interpolate.splev(u, tck)

    # Move cursor
    duration = Constants.CursorTimeDelay
    for point in zip(*(i.astype(int) for i in points)):
        pyautogui.platformModule._moveTo(int(point[0]), int(point[1]))
        if (point[0] % 14 == 0):
            time.sleep(duration)

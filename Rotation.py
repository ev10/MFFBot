import time

import Keystroke
import Constants

class Attack:
    def __init__(self, cooldown, delay, priority, key):
        self.cd = cooldown
        self.pr = priority
        self.dl = delay
        self.key = key

    def activate(self):
        Keystroke.press(self.key)
        time.sleep(self.dl)

class Rotation:
    def __init__(self, attacks):
        self.atk = attacks

    def exec(self):
        for i in self.atk:
            i.activate()

def start_rotation():
    time.sleep(5)
    #Sk1 = Attack(6,0,5,0x41)
    Sk2 = Attack(11, 0.2, 4, 0x42)
    Sk3 = Attack(18, 0.5, 2, 0x43)
    Sk4 = Attack(16, 2,   3, 0x44)
    Sk5 = Attack(14, 2.5, 1, 0x45)
    SkList = [Sk2, Sk3, Sk4, Sk5]
    SkList.sort(key=lambda y: int(y.pr))
    DefaultRot = Rotation(SkList)
    while True:
        DefaultRot.exec()
        time.sleep(Constants.SCTimeDelay)


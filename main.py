import cv2 as cv
import numpy as np
import time
from windowcapture import WindowCapture
from pynput.keyboard import Key, Controller
keyboard = Controller()
found = False
#Change Name fivem Server
wincap = WindowCapture('FiveM - Test_m_server')

lower = [0, 0, 150]
upper = [20, 20, 255]
lower = np.array(lower, dtype = "uint8")
upper = np.array(upper, dtype = "uint8")

numofReset = 4
numofsuc = 0
    

while(True):
    screenshot = wincap.get_screenshot()
    mask = cv.inRange(screenshot, lower, upper)
    output = cv.bitwise_and(screenshot, screenshot, mask = mask)
    cv.imshow('images', np.hstack([screenshot, output]))

    x = output[10] #center
    for i in range(len(output[10])):
        n = x[i]
        value = n[2]
        # print(value)
        if n[2] > 0:
            found = True
        

    if found:
        found = False
        keyboard.press('e')
        keyboard.release('e')
        time.sleep(0.15)
    
    # if numofsuc >= numofReset:
    #     print("NEW LOOP")
    #     time.sleep(4)
    #     print("m")

    #     keyboard.press('m')
    #     # time.sleep(3)
    #     numofsuc = 0




    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


print('DONE.')
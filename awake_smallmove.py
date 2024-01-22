import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = False #stops script of the mouse is in the upper left corner of the screen
numMin = None

#CLI arugment can be specified for the time period between action others defaults to 3 minutes
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3
else:
    numMin = int(sys.argv[1])

while(True):
    x=0

    while(x<numMin):
        time.sleep(60)
        x+=1
    
    # Get the current mouse position
    #current_x, current_y = pyautogui.position()

    # Move the mouse a very small amount
    #pyautogui.moveTo(current_x + 3, current_y + 3)

    # Wait for a short time
    #time.sleep(0.1)

    # Move the mouse back to the original position
    #pyautogui.moveTo(current_x, current_y)
    
    pyautogui.moveRel(3,3)
    for i in range(0,3):
        pyautogui.press("shift")
        time.sleep(0.1)

    print("Movement made at {}".format(datetime.now().time()))
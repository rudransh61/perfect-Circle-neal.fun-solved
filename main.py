import pyautogui
import math

R = 200
(x,y) = pyautogui.size()
(X,Y) = pyautogui.position(x/2,y/2)
pyautogui.moveTo(X+R,Y)

for i in range(1000):
    if i%6==0:
       pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
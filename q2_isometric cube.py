import pyautogui, time
side=20
time.sleep(5)
pyautogui.dragRel(0,200,duration=0.5)
for i in range(0,side,1):
    y=0.57735026*i
    pyautogui.dragRel(i,y,duration=0.1)
pyautogui.dragRel(0,-200,duration=0.5)
for i in range(0,side,1):
    y=0.57735026*i
    pyautogui.dragRel(-i,-y,duration=0.1)
for i in range(0,side,1):
    y=0.57735026*i
    pyautogui.dragRel(i,-y,duration=0.1)
for i in range(0,side,1):
    y=0.57735026*i
    pyautogui.dragRel(i,y,duration=0.1)
for i in range(0,side,1):
    y=0.57735026*i
    pyautogui.dragRel(-i,y,duration=0.1)
pyautogui.dragRel(0,200,duration=0.5)
for i in range(0,side,1):
    y=0.57735026*i
    pyautogui.dragRel(i,-y,duration=0.1)
pyautogui.dragRel(0,-200,duration=0.5)

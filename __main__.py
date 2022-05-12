from asyncio import subprocess
import pyautogui
import os
import subprocess
from playwright.sync_api import Playwright, sync_playwright
import time

def terminalSetup():
    os.system("rmmod v4l2loopback")
    time.sleep(1)
    os.system("modprobe v4l2loopback devices = 4")
    os.system("v4l2-ctl --list-devices")
    print("devices created")
def setupZoom():
    pyautogui.press('win')
    pyautogui.write('zoom')
    pyautogui.press('enter')
    time.sleep(1)
    while True:
        #locate room button
        position = pyautogui.locateOnScreen('buttons\\startMeetingCam.png')
        if position != None:
            pyautogui.click(position)
            print("Clicked new room")
            break
        elif position == None:
            print("Could not find new room")
            print("checking for other button")
            position = pyautogui.locateOnScreen('buttons\\startMeetingNoCam.png')
            if position != None:
                pyautogui.click(position)
                print("clicked new room")
                time.sleep(5)
                print("turning on camera")
                pyautogui.keyDown('altleft'); pyautogui.press('v'); pyautogui.keyUp('altleft')
                break
        else:
            time.sleep(1)
            print("no button found trying again")
def chatZoom(message,chatOpen):
    #sending chat
    
    if chatOpen == False :
        time.sleep(5)
        pyautogui.keyDown('altleft'); pyautogui.press('h'); pyautogui.keyUp('altleft')
        print('chat opened')
        time.sleep(0.5)
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        chatOpen == True
       
    else:
        time.sleep(0.5)
        pyautogui.typewrite(message)
        pyautogui.press('enter')
def creatBot(botName,modelStep):
    terminalSetup()
    # run terminal commands 
    subprocess.run(botCreate.py, botName, modelStep)
#terminalSetup()
#print("terminal setup done")
#setupZoom()
#print("zoom room setup")
creatBot("bottest")
#print("bots created")

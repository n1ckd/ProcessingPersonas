from socket import timeout
import time
import os
from playwright.sync_api import sync_playwright
botName = "observation"
modelStep = 1
roomCode = "" # laptop code
#print("subprocess runnning")    

def run(playwright, botName):
        browser = playwright.chromium.launch(headless=False, slow_mo =100,timeout=300000) #5min timeout
        context = browser.new_context(
            permissions=["camera","microphone"]
        )
    #open join page
        page = context.new_page()
        page.goto("https://zoom.us/wc/join/" + roomCode )
        time.sleep(1)
    #enter name
        page.click("[placeholder=\"Your Name\"]")
        page.fill("[placeholder=\"Your Name\"]", botName)
        time.sleep(1)
    #join room
        page.click("button:has-text(\"Join\")")
        print("button pressed")
        time.sleep(30)
        page.keyboard.press("Alt+v")#turn on video
        page.keyboard.press("Alt+n")#cycle video
        
        #join audio
        
def imageSetup(modelStep):
    print(modelStep)
    if modelStep == 1:
        print("observation persona")
        topLeftCam ='images\\observe1.png'
        topRightCam = 'images\\observe2.png'
        bottomLeftCam = 'images\\observe3.png'
        bottomRightCam = 'images\\observe4.png'
    elif modelStep == 2:
        print("algorithm persona")
        topLeftCam = 'images\\algorithm1.png'
        topRightCam = 'images\\algorithm2.png'
        bottomLeftCam = 'images\\algorithm3.png'
        bottomRightCam = 'images\\algorithm4.png'
    elif modelStep == 3:
        print("results persona")
        topLeftCam = 'images\\result1.png'
        topRightCam = 'images\\result2.png'
        bottomLeftCam = 'images\\result3.png'
        bottomRightCam = 'images\\result4.png'
    elif modelStep == 4:
        print("consequences persona")
        topLeftCam = 'images\\consequence1.png'
        topRightCam = 'images\\consequence2.png'
        bottomLeftCam = 'images\\consequence3.png'
        bottomRightCam = 'images\\consequence4.png'
    else:
        print(modelStep)
        print("needs to be 1,2,3,or 4")

    #ffmpeg commands
    print("ffmpeg v4l2" + topLeftCam + "dev/video_0")
    print("ffmpeg v4l2" + topRightCam + "dev/video_2")
    print("ffmpeg v4l2" + bottomLeftCam + "dev/video_2")
    print("ffmpeg v4l2" + bottomRightCam + "dev/video_3")
with sync_playwright() as playwright:
    run(playwright, botName)
#imageSetup(modelStep)

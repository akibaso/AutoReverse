from resource.ADB import *
from resource.Image.pattern import *
from resource.Image.OCR import *
import subprocess
import time

packagename = 'com.shenlan.m.reverse1999'
activityCN = 'com.shenlan.m.reverse1999/com.ssgame.mobile.gamesdk.frame.AppStartUpActivity'
emulator= r"D:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuPlayer.exe -v 0"
screencaptime = 3

def startup(host,port,emulator,sleep,screencaptime):
    stage = "start"
    subprocess.Popen(emulator)
    #time.sleep(sleep)
    try:
        device = connect(host,port)
    except:
        print("ADB ERROR")
        return
    device.shell("am start "+activityCN)
    time.sleep(3)
    while stage == "start":
        ret = pattern(screenshot(device),"START")
        if ret!=0:
            stage = "login"
            return ret,device,stage
        time.sleep(screencaptime)

def login(ret,device,stage):
    if stage == "login":
        tap(ret[0],ret[1],device)
        time.sleep(3)
        stage = "main"
        return stage
def fight(device,screencaptime,stage):
    ret = pattern(screenshot(device),"BACK")
    if ret!=0:
        stage = "unknown"
        while stage != "main":
            ret = pattern(screenshot(device),"BACK")
            if ret!=0:
                tap(ret[0],ret[1],device)
                time.sleep(screencaptime)
            elif ret == 0:
                stage = "main"

    if stage == "main":
        ret = pattern(screenshot(device),"FIGHT")
        tap(ret[0],ret[1],device)

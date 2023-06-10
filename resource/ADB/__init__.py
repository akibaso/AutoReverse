from adb_shell.adb_device import AdbDeviceTcp
import cv2
def connect(host,port):
    device = AdbDeviceTcp(host,port)
    device.connect()
    return device
def screenshot(device):
    device.shell("screencap -p /sdcard/screen.png")
    device.pull("/sdcard/screen.png","screen.png")
    img = "screen.png"
    return img
def tap(x,y,device):
    device.shell(f"input tap {x} {y}")
def swipe(x1,y1,x2,y2,device):
    device.shell(f"input swipe {x1} {y1} {x2} {y2}")
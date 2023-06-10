import cv2
import numpy as np
from matplotlib import pyplot as plt
templates = {"START":"START.png","LOADING2":"Loading2.png","FIGHT":"Fight.png","BACK":"BACK.png"}
def pattern(img,template):
    img = cv2.imread(img)
    if template in templates:
        pattern = cv2.imread("resource/Image/pattern/template/"+templates[template], 0)
    else:
        return 1
    w, h = pattern.shape[::-1]
    method = cv2.TM_CCORR_NORMED
    res = cv2.matchTemplate(img, pattern, method)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    print(top_left,max_val)
    if max_val > 0.8:
        return top_left
    else:
        return 0


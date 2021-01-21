import numpy as np
import cv2

def HSItest(args, img):
    imgRoi = img[args.x:args.x + args.w, args.y:args.y + args.h]
    h, s, i = cv2.split(imgRoi)
    brightness = np.mean(i)
    return brightness, i
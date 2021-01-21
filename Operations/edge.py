import cv2
import numpy as np

def edgeLocation(args, img):
    img = img[args.x:args.x + args.w, args.y:args.y + args.h]
    edges = cv2.Canny(img, args.mintresh, args.maxtresh)
    coordinates = np.argmax(edges, axis=0)
    value = 0.754806 * coordinates - 2.74455
    return value, edges


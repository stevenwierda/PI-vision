import cv2
import numpy as np
import os


class Saver:
    def __init__(self, args):
        self.args = args

    def saveImage(self, img):
        name = input("enter file name and extention")
        cv2.imwrite(name, img)

    def SaveNPY(self, img, i):
        name = input("enter file name")
        #name = "edge" + str(i)
        np.save("C:\\Users\\Steven\\Documents\\PI\\vision\\PI-vision\\Images\\dataset2\\" + name + ".npy", img)

    def imageCropper(self, img):
        y = img.shape[1]
        x = img.shape[2]
        imgCropped = img[y:self.args.y + self.args.h, x:self.args.x + self.args.w]
        return imgCropped

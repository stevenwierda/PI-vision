import argparse
# from imageGetter.imageAccusition import imageAccusitionCamera
from imageGetter.imageAccusition import imageAccusitionFile
from imageSaver.saver import Saver
import cv2
import numpy as np
import os
import time


def parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    """The image framework"""
    parser.add_argument("-getImageMethode", type=str, help="getting image via the camera or file",
                        choices=["camera", "file"], default="file")
    parser.add_argument("--outputType", type=str, help="determine the output", choices=["console", "OPC", "Image"],
                        default="console")

    """Dit zijn de instellingen voor de OPC Client"""
    parser.add_argument("--ip", type=str, help="the ip form the PLC", default="192.168.1.10")
    parser.add_argument("--Password", type=str, help="password of the PLC", default="ba7432c5")
    parser.add_argument("--username", type=str, help="username for the PLC", default="admin")
    parser.add_argument("--nodeID", type=str, help="node of the variable for the PLC", default="ns=4;")

    """Dit zijn de instelling voor de fileLoader"""
    parser.add_argument("--datasetLocationTxt", type=str, help="location of the file",
                        default="C:\\Users\\steve\\OneDrive\\Documents\\GitHub\\PI-vision\\Imagelist\\refractormeter.txt")
    parser.add_argument("--datasetLocation", type=str, help="location of the images",
                        default="C:\\Users\\steve\\OneDrive\\Documents\\GitHub\\PI-vision\\Images")
    parser.add_argument("--test", type=str, help="test", default="test")

    """Dit zijn de instellingen voor de file saver"""
    parser.add_argument("--file", type=str, help="the output file type", choices=["npy", "png"], default="png")
    parser.add_argument("--x", type=int, help="start x pixel of the crop", default=255)
    parser.add_argument("--y", type=int, help="start y pixel of the crop", default=759)
    parser.add_argument("--h", type=int, help="height of the cropped image", default=494)
    parser.add_argument("--w", type=int, help="with of the cropped image", default=753)
    return parser.parse_args()


def getImageMethode(args):
    if args.getImageMethode == "file":
        imageGetter = imageAccusitionFile(args)
    # elif args.getImageMethode == "camera":
    # imageGetter = imageAccusitionCamera(args)
    else:
        raise Exception('Unknown framework (image)')
    return imageGetter


def imageOperations(args, img):
    imgRoi = img[args.x:args.x + args.w, args.y:args.y + args.h]
    h, s, i = cv2.split(imgRoi)
    brightness = np.mean(h)
    #brix = 0.8928 * brightness + 4.9968
    return h, brightness


def main(args):
    imageGetter = getImageMethode(args)
    imageSaver = Saver(args)
    for i in range(0, len(imageGetter.selec_img)):
        img = imageGetter.load_img(i)
        img = imageGetter.RGB_TO_HSI(img, i)
        img, brightness = imageOperations(args, img)
        print("the brightness = ", brightness)
        imageSaver.SaveNPY(img, i)

    # images = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)


if __name__ == '__main__':
    main(parser())

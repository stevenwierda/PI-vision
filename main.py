import argparse
from imageAccusition import imageAccusition
import numpy as np
import cv2
import PIL


def parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-ip", type=str, help="the ip form the PLC", default="192.168.1.10")
    parser.add_argument("--Password", type=str, help="password of the PLC", default="")
    parser.add_argument("--username", type=str, help="username for the PLC", default="admin")
    return parser.parse_args()


def main(args):
    imageGetter = imageAccusition(args)
    img = imageGetter.getImage()
    #images = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

    cv2.imwrite("brix040.png", img)


if __name__ == '__main__':
    main(parser())

import argparse
#from imageGetter.imageAccusition import imageAccusitionCamera
from Operations.brightness import HSItest
from Operations.edge import edgeLocation
from imageGetter.imageAccusition import imageAccusitionPNG
from imageSaver.saver import Saver
from communication.OPC import OPC
import cv2
import numpy as np


def parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    """The image framework"""
    parser.add_argument("-getImageMethode", type=str, help="getting image via the camera or file",
                        choices=["camera", "file"], default="file")
    parser.add_argument("-getImageFileFormat", type=str, help="iamge extention",
                        choices=["npy", "png"], default="png")
    parser.add_argument("--outputType", type=str, help="determine the output", choices=["console", "OPC", "Image"],
                        default="console")
    parser.add_argument("--clrSpec", type=str, choices=["RGB", "HSI"], default="RGB")
    parser.add_argument("--operations", type=str, choices=["ëdge", "brightness"], default="edge")

    """Dit zijn de instellingen voor de OPC Client"""
    parser.add_argument("--ip", type=str, help="the ip form the PLC", default="192.168.1.10")
    parser.add_argument("--Password", type=str, help="password of the PLC", default="ba7432c5")
    parser.add_argument("--username", type=str, help="username for the PLC", default="admin")
    parser.add_argument("--nodeID", type=str, help="node of the variable for the PLC", default="ns=4;")

    """Dit zijn de instelling voor de fileLoader"""
    parser.add_argument("--datasetLocationTxt", type=str, help="location of the file",
                        default="C:\\Users\\Steven\\Documents\\PI\\vision\\PI-vision\\Imagelist\\refractometer2.txt")
    parser.add_argument("--datasetLocation", type=str, help="location of the images",
                        default="C:\\Users\\Steven\\Documents\\PI\\vision\\PI-vision\\Images\\dataset2")
    parser.add_argument("--test", type=str, help="test", default="test")

    """Dit zijn de instellingen voor de file saver"""
    parser.add_argument("--file", type=str, help="the output file type", choices=["npy", "png"], default="png")

    """image cropping"""
    parser.add_argument("--x", type=int, help="start x pixel of the crop", default=197)
    parser.add_argument("--y", type=int, help="start y pixel of the crop", default=388)
    parser.add_argument("--h", type=int, help="height of the cropped image", default=1)
    parser.add_argument("--w", type=int, help="with of the cropped image", default=219)

    """Edge detection instellingen"""
    parser.add_argument("--mintresh", type=int, help="the lower threshold value", default=50)
    parser.add_argument("-maxtresh", type=int, help="the upper treshhold value", default=150)

    return parser.parse_args()


def getImageMethode(args):
    if args.getImageMethode == "file":
        imageGetter = imageAccusitionPNG(args)
    # elif args.getImageMethode == "camera":
    # imageGetter = imageAccusitionCamera(args)
    else:
        raise Exception('Unknown framework (image)')
    return imageGetter

def imageOperations(args, img):
    if args.operations == "brightness":
        value, img = HSItest(args, img)
    elif args.operations == "edge":
        value, img = edgeLocation(args, img)
    else:
        raise Exception("unkown task")
    return img, value



def main(args):
    opc = OPC(args)
    imageGetter = getImageMethode(args)
    imageSaver = Saver(args)
    for i in range(0, len(imageGetter.selec_img)):
        img = imageGetter.load_img(i)
        img, value = imageOperations(args, img)
        print("the value = ", value)
        imageSaver.SaveNPY(img, i)
        opc.setValue("ns=4;s=Arp.Plc.Eclr/refratoreadout1.OPCvalue", value)
    opc.disconnect()
    # images = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)



if __name__ == '__main__':
    main(parser())

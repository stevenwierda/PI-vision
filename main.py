import argparse
from imageGetter.imageAccusition import imageAccusitionCamera
from imageGetter.imageAccusition import imageAccusitionFile
import cv2


def parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    """The image framework"""
    parser.add_argument("-getImageMethode", type=str, help="getting image via the camera or file",
                        choices=["camera", "file"], default="file")
    parser.add_argument("--outputType", type=str, help="determine the output", choices=["console", "OPC"],
                        default="console")

    """Dit zijn de instellingen voor de OPC Client"""
    parser.add_argument("--ip", type=str, help="the ip form the PLC", default="192.168.1.10")
    parser.add_argument("--Password", type=str, help="password of the PLC", default="ba7432c5")
    parser.add_argument("--username", type=str, help="username for the PLC", default="admin")
    parser.add_argument("--nodeID", type=str, help="node of the variable for the PLC", default="ns=4;")

    """Dit zijn de instelling voor de fileLoader"""
    parser.add_argument("--datasetLocation", type=str, help="location of the file", default="../imagelist/dataset1.txt")
    parser.add_argument("--test", type=str, help="test", default="test")

    return parser.parse_args()


def getImageMethode(args):
    if args.getImageMethode == "file":
        imageGetter = imageAccusitionFile(args)
    elif args.getImageMethode == "camera":
        imageGetter = imageAccusitionCamera(args)
    else:
        raise Exception('Unknown framework (image)')
    return imageGetter


def main(args):
    imageGetter = imageAccusitionCamera(args)
    img = imageGetter.getImage()
    # images = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

    cv2.imwrite("brix040.png", img)


if __name__ == '__main__':
    main(parser())

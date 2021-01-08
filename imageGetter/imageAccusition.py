from picamera import PiCamera
from picamera.array import PiRGBArray

import numpy as np
import os
import cv2


class imageAccusitionCamera():
    def __init__(self, args):
        self.camera = PiCamera()
        #self.camera.resolution(200, 200)
        self.cameraArray = PiRGBArray(self.camera)

    def __getitem__(self):
        self.camera.capture(self.cameraArray, format="bgr")
        img = self.cameraArray.array
        return img

class imageAccusitionFile():
    def __init__(self, args):
        self.args = args
        self.imgPath = os.path.join(self.args.dataset, args.imgs)

        with open(os.path.join(args.datasetLocation, self.mode[0] + '.txt'), 'r') as file:
            lines = file.read().splitlines()  # list of the txt file's lines
        for img_name in lines:
            impath = os.path.join(self.img_path, img_name + ".npy")
            mpath = os.path.join(self.mask_path, img_name + ".png")

            self.selec_img.append(impath)
            self.selec_mask.append(mpath)

        if len(self.selec_img) == 0:
            raise Exception("no Image")

        assert (len(self.selec_img) == len(self.selec_mask))
        print("\nNumber of images to be processed in is: {:d}".format(len(self.selec_img)))

    def __getitem__(self):

        img = self.transforms(self.load_img(index)).float()

    def load_img(self, index):
        # In Plastic dataset: HxWxC ---> transpose to CxHxW
        # img = np.transpose(np.load(self.selec_img[index]),[2,0,1])
        img = np.load(self.selec_img[index])
        print("this is the shape of the image", img.shape)
        return img



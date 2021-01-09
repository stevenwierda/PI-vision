"""from picamera import PiCamera
from picamera.array import PiRGBArray"""

import numpy as np
import os
import cv2
import math


"""class imageAccusitionCamera():
    def __init__(self, args):
        self.camera = PiCamera()
        #self.camera.resolution(200, 200)
        self.cameraArray = PiRGBArray(self.camera)

    def __getitem__(self):
        self.camera.capture(self.cameraArray, format="bgr")
        img = self.cameraArray.array
        return img"""

class imageAccusitionFile():
    def __init__(self, args):
        self.args = args
        self.imgPath = os.path.join(self.args.datasetLocation)

        self.selec_img = []

        with open(os.path.join(args.datasetLocationTxt), 'r') as file:
            lines = file.read().splitlines()  # list of the txt file's lines
        for img_name in lines:
            impath = os.path.join(self.imgPath, img_name + ".png")

            self.selec_img.append(impath)

        if len(self.selec_img) == 0:
            raise Exception("no Image")

        print("\nNumber of images to be processed in is: {:d}".format(len(self.selec_img)))

    def __getitem__(self, index):
        img = self.load_img(index)
        return img

    def load_npy(self, index):
        # In Plastic dataset: HxWxC ---> transpose to CxHxW
        # img = np.transpose(np.load(self.selec_img[index]),[2,0,1])
        img = np.load(self.selec_img[index],allow_pickle=True)
        print("this is the shape of the image", img.shape)
        return img

    def load_img(self, index):
        img = cv2.cvtColor(cv2.imread(self.selec_img[index]), cv2.COLOR_BGR2RGB)
        cv2
        print("this is the shape of the image", img.shape)
        return img

    def RGB_TO_HSI(self, img, index):
        with np.errstate(divide='ignore', invalid='ignore'):

            # Load image with 32 bit floats as variable type
            bgr = np.float32(img) / 255

            # Separate color channels
            blue = bgr[:, :, 0]
            green = bgr[:, :, 1]
            red = bgr[:, :, 2]

            # Calculate Intensity
            def calc_intensity(red, blue, green):
                return np.divide(blue + green + red, 3)

            # Calculate Saturation
            def calc_saturation(red, blue, green):
                minimum = np.minimum(np.minimum(red, green), blue)
                saturation = 1 - (3 / (red + green + blue + 0.001) * minimum)

                return saturation

            # Calculate Hue
            def calc_hue(red, blue, green):
                hue = np.copy(red)

                for i in range(0, blue.shape[0]):
                    for j in range(0, blue.shape[1]):
                        hue[i][j] = 0.5 * ((red[i][j] - green[i][j]) + (red[i][j] - blue[i][j])) / \
                                    math.sqrt((red[i][j] - green[i][j]) ** 2 +
                                              ((red[i][j] - blue[i][j]) * (green[i][j] - blue[i][j])))
                        hue[i][j] = math.acos(hue[i][j])

                        if blue[i][j] <= green[i][j]:
                            hue[i][j] = hue[i][j]
                        else:
                            hue[i][j] = ((360 * math.pi) / 180.0) - hue[i][j]
                return hue

            # Merge channels into picture and return image
            hsi = cv2.merge(
                (calc_hue(red, blue, green), calc_saturation(red, blue, green), calc_intensity(red, blue, green)))
            np.save("C:\\Users\\steve\\OneDrive\\Documents\\GitHub\\PI-vision\\Images\\hsi" + str(index) + ".npy", hsi)
            return hsi



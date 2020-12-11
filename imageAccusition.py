from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2


class imageAccusition():
    def __init__(self, args):
        self.camera = PiCamera()
        #self.camera.resolution(200, 200)
        self.cameraArray = PiRGBArray(self.camera)

    def getImage(self):
        self.camera.capture(self.cameraArray, format="bgr")
        img = self.cameraArray.array
        return img

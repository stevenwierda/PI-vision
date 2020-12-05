from picamera import PiCamera
from picamera.array import PiRGBArray


class imageAccusition():
    def __init__(self, args):
        self.camera = PiCamera()
        self.camera.resolution(200, 200)
        self.cameraArray = PiRGBArray(self.camera)

    def getImage(self):
        img = self.camera.capture(self.cameraArray, format="bgr")
        return img

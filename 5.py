

import numpy as np
import cv2

def take_photo():
    cap = cv2.VideoCapture(0)
    ret, photo = cap.read()
    if ret:
        print "take photo successfuly"
        cv2.imwrite("./photo.jpg", photo)
    else:
        print "Error! Photo failed!"


if __name__ == "__main__":
    take_photo()

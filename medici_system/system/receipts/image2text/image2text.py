import cv2
import numpy
import datetime

def image2text(image):
    img = cv2.imdecode(numpy.fromstring(image, numpy.uint8), 1)
    path = '/tmp/' + str(datetime.datetime.now()) + '.jpg'
    cv2.imwrite(path, img)

    return '0'

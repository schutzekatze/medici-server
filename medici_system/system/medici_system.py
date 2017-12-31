from decimal import Decimal
from .receipts.receipt2text.ocr_inference import inference
import cv2
import numpy

def receipt_image(mediciuser, image):
    img = cv2.imdecode(numpy.fromstring(image, numpy.uint8), 1)
    cv2.imwrite('tmp.jpg', img)
    text = inference('tmp.jpg')

    print(text)

    return text

def receipt_text(mediciuser, text):
    pass

def receipt_json(mediciuser, json):
    pass

def user_create(user_info):
    pass

def user_update(mediciuser, user_info):
    pass

def user_last_updated(mediciuser):
    return 'Not implemented.'

def user_fetch(mediciuser):
    return 'Not implemented'

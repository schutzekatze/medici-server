from decimal import Decimal
from .receipts.image2text.image2text import image2text
from .receipts.text2json.text2json import text2json

def receipt_image(mediciuser, image):
    text = image2text(image)
    json = text2json(text)

    mediciuser.balance += Decimal(json)
    mediciuser.save()

def receipt_text(mediciuser, text):
    pass

def receipt_json(mediciuser, json):
    pass

def user_create(user_info):
    pass

def user_update(mediciuser, user_info):
    mediciuser.balance = Decimal(user_info)
    mediciuser.save()

def user_last_updated(mediciuser):
    return 'Not implemented.'

def user_fetch(mediciuser):
    return str(mediciuser.balance)

from .receipts.image2text.image2text import image2text
from .receipts.text2json.text2json import text2json
from .user_manager import user_manager
from .item_manager import item_manager

SUCESS_MESSAGE = 'Success'

def receipt_image(mediciuser, image):
    text = image2text(image)
    json = text2json(text)

    user_change_info = user_manager.process_receipt_json(json)
    item_manager.process_receipt_json(json)

    return user_change_info

def receipt_text(mediciuser, text):
    json = text2json(text)

    user_change_info = user_manager.process_receipt_json(json)
    item_manager.process_receipt_json(json)

    return user_change_info

def receipt_json(mediciuser, json):
    user_change_info = user_manager.process_receipt_json(json)
    item_manager.process_receipt_json(json)

    return user_change_info

def user_create(user_info):
    user_manager.user_create(user_info)

    return SUCESS_MESSAGE

def user_update(mediciuser, user_info):
    user_manager.user_update(mediciuser, user_info)

    return SUCESS_MESSAGE

def user_last_updated(mediciuser):
    return user_manager.user_last_updated(mediciuser)

def user_fetch(mediciuser):
    return user_manager.user_fetch(mediciuser)

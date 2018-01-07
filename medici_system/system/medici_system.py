from .receipts.image2text.image2text import image2text
from .receipts.text2data.text2data import text2data
from .user_manager import user_manager
from .item_manager import item_manager
import logging

logger = logging.getLogger("Medici System")

SUCESS_MESSAGE = "Success"

def process_data(mediciuser, data):
    user_change_data = user_manager.process_receipt_data(mediciuser, data)
    item_manager.process_receipt_data(data)

    return user_change_data

def receipt_image(mediciuser, image):
    logger.info("Received receipt image from <" + mediciuser.user.username + ">")

    text = image2text(image)
    data = text2data(text)

    user_change_data = process_data(mediciuser, data)

    return SUCCESS_MESSAGE

def receipt_text(mediciuser, text):
    logger.info("Received receipt text from <" + mediciuser.user.username + ">")

    text = text['receipt_text']
    data = text2data(text)

    user_change_data = process_data(mediciuser, data)

    return SUCCESS_MESSAGE

def receipt_data(mediciuser, data):
    logger.info("Received receipt data from <" + mediciuser.user.username + ">")

    data = data['receipt_data']
    user_change_data = process_data(mediciuser, data)

    return SUCCESS_MESSAGE

def user_create(user_data):
    logger.info("Received user create request for <" + user_data['username'] + ">")

    user_data = user_data['user_data']
    mediciuser = user_manager.user_create(user_data)

    return SUCESS_MESSAGE

def user_update(mediciuser, user_data):
    logger.info("Received user update request from <" + mediciuser.user.username + ">")

    user_data = user_data['user_data']
    user_manager.user_update(mediciuser, user_data)

    return SUCESS_MESSAGE

def user_fetch(mediciuser, user_fields):
    logger.info("Received user fetch request from <" + mediciuser.user.username + ">")

    user_fields = user_fields['user_fields']
    return user_manager.user_fetch(mediciuser, user_fields)

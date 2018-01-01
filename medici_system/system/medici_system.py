from .receipts.image2text.image2text import image2text
from .receipts.text2json.text2json import text2json
from .user_manager import user_manager
from .item_manager import item_manager

import logging

logger = logging.getLogger('Medici System')

SUCESS_MESSAGE = 'Success'

def process_json(json):
    user_change_info = user_manager.process_receipt_json(json)
    item_manager.process_receipt_json(json)

    return user_change_info

def receipt_image(mediciuser, image):
    logger.info('Received receipt image from: ' + mediciuser.user.username)

    text = image2text(image)
    json = text2json(text)

    return process_json(json)

def receipt_text(mediciuser, text):
    logger.info('Received receipt text from: ' + mediciuser.user.username)

    json = text2json(text)

    return process_json(json)

def receipt_json(mediciuser, json):
    logger.info('Received receipt json from: ' + mediciuser.user.username)

    return process_json(json)

def user_create(user_info):
    logger.info('Creating user: ' + mediciuser.user.username)

    mediciuser = user_manager.user_create(user_info)

    return SUCESS_MESSAGE

def user_update(mediciuser, user_info):
    logger.info('Updating user: ' + mediciuser.user.username)

    user_manager.user_update(mediciuser, user_info)

    return SUCESS_MESSAGE

def user_last_updated(mediciuser):
    logger.info('Getting user last updated: ' + mediciuser.user.username)

    return user_manager.user_last_updated(mediciuser)

def user_fetch(mediciuser):
    logger.info('Fetching user: ' + mediciuser.user.username)

    return user_manager.user_fetch(mediciuser)

import logging

logger = logging.getLogger('User Manager')

def process_receipt_json(json):
    logger.info('Received json: ' + json)

def user_create(user_info):
    pass

def user_update(mediciuser, user_info):
    pass

def user_last_updated(mediciuser):
    return ''

def user_fetch(mediciuser):
    return ''

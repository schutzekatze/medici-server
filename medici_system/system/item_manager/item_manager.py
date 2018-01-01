import logging

logger = logging.getLogger('Item Manager')

def process_receipt_json(json):
    logger.info('Received json: ' + json)

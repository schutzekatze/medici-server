import logging

logger = logging.getLogger('Item Manager')

def process_receipt_data(data):
    logger.info("Received data:\n" + data + "\nProcessing...")

    logger.info("Data processed successfully.")

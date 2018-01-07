import logging

logger = logging.getLogger(__name__)

def process_receipt_data(data):
    logger.info("Received data:\n" + str(data) + "\nProcessing...")

    logger.info("Data processed successfully.")

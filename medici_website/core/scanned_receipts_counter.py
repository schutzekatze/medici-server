import os

def get_scanned_receipts_count():
    return len(os.listdir('/home/flux/receipts-unlabeled'))

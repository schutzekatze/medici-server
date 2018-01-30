import os

def get_scanned_receipts_count():
    count = 0

    for _, _, filenames in os.walk('/home/flux/receipts/unlabeled'):
        count += len(filenames)

    for _, _, filenames in os.walk('/home/flux/receipts/labeled-seg'):
        count += len(filenames)

    return count

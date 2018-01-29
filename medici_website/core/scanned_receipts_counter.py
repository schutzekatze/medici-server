import glob

def get_scanned_receipts_count():
    return len(glob.glob('/tmp/cenec*'))

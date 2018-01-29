from django.shortcuts import render

from .core.scanned_receipts_counter import get_scanned_receipts_count

def index(request):
    context = { 'scanned_receipts_count': get_scanned_receipts_count() }
    return render(request, 'medici_website/index.html', context)

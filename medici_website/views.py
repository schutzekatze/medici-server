from django.shortcuts import render

def index(request):
    return render(request, 'medici_website/index.html')

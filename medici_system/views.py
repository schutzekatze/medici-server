from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied

from .system import medici_system

def check_post(request):
    if request.method != 'POST':
        raise Http404

def check_auth(request):
    if request.user.is_authenticated:
        return request.user.mediciuser

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is None:
        raise PermissionDenied

    login(request, user)
    return request.user.mediciuser

def receipt_image(request):
    check_post(request)
    mediciuser = check_auth(request)

    image = request.FILES['image']
    medici_system.receipt_image(mediciuser, image)

    return HttpResponse('Success.')

def receipt_text(request):
    check_post(request)
    mediciuser = check_auth(request)

    text = request.FILES['text']
    medici_system.receipt_text(mediciuser, text)

    return HttpResponse('Success.')

def receipt_json(request):
    check_post(request)
    mediciuser = check_auth(request)

    json = request.FILES['json']
    medici_system.receipt_json(mediciuser, json)

    return HttpResponse('Success.')

def user_create(request):
    check_post(request)

    user_info = request.POST['user_info']
    medici_system.user_create(user_info)

    return HttpResponse('Success.')

def user_update(request):
    check_post(request)
    mediciuser = check_auth(request)

    user_info = request.POST['user_info']
    medici_system.user_update(mediciuser, user_info)

    return HttpResponse('Success.')

def user_last_updated(request):
    check_post(request)
    mediciuser = check_auth(request)

    return HttpResponse(medici_system.user_last_updated(mediciuser))

def user_fetch(request):
    check_post(request)
    mediciuser = check_auth(request)

    return HttpResponse(medici_system.user_fetch(mediciuser))

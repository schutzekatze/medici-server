from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.conf import settings
from .system import medici_system
import os
import configparser
import json

medici_config = configparser.ConfigParser()
medici_config.read(os.path.join(settings.BASE_DIR, 'medici_system/system/medici_config/medici.ini'))

USER_USERNAME_PARAMETER = medici_config['communication']['user_username_param']
USER_PASSWORD_PARAMETER = medici_config['communication']['user_password_param']
USER_DATA_PARAMETER = medici_config['communication']['user_data_param']
USER_FIELDS_PARAMETER = medici_config['communication']['user_fields_param']

RECEIPT_IMAGE_PARAMETER = medici_config['communication']['receipt_image_param']
RECEIPT_TEXT_PARAMETER = medici_config['communication']['receipt_text_param']
RECEIPT_DATA_PARAMETER = medici_config['communication']['receipt_data_param']

def check_post(request):
    if request.method != 'POST':
        raise Http404

def check_auth(request):
    if request.user.is_authenticated:
        return request.user.mediciuser

    username = request.POST[USER_USERNAME_PARAMETER]
    password = request.POST[USER_PASSWORD_PARAMETER]
    user = authenticate(request, username=username, password=password)
    if user is None:
        raise PermissionDenied

    login(request, user)
    return request.user.mediciuser

def user_create(request):
    check_post(request)

    user_data = json.loads(request.POST[USER_DATA_PARAMETER])
    response = medici_system.user_create(user_data)
    response = json.dumps(response)

    return HttpResponse(response)

def user_update(request):
    check_post(request)
    mediciuser = check_auth(request)

    user_data = json.loads(request.POST[USER_DATA_PARAMETER])
    response = medici_system.user_update(mediciuser, user_data)
    response = json.dumps(response)

    return HttpResponse(response)

def user_fetch(request):
    check_post(request)
    mediciuser = check_auth(request)

    user_fields = json.loads(request.POST[USER_FIELDS_PARAMETER])
    response = medici_system.user_fetch(mediciuser, user_fields)
    response = json.dumps(response)

    return HttpResponse(response)

def receipt_image(request):
    check_post(request)
    mediciuser = check_auth(request)

    image = request.FILES[RECEIPT_IMAGE_PARAMETER]
    response = medici_system.receipt_image(mediciuser, image)
    response = json.dumps(response)

    return HttpResponse(response)

def receipt_text(request):
    check_post(request)
    mediciuser = check_auth(request)

    text = request.POST[RECEIPT_TEXT_PARAMETER]
    response = medici_system.receipt_text(mediciuser, text)
    response = json.dumps(response)

    return HttpResponse(response)

def receipt_data(request):
    check_post(request)
    mediciuser = check_auth(request)

    data = json.loads(request.POST[RECEIPT_DATA_PARAMETER])
    response = medici_system.receipt_data(mediciuser, data)
    response = json.dumps(response)

    return HttpResponse(response)

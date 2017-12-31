from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.conf import settings

from .system import medici_system

import os
import configparser
medici_config = configparser.ConfigParser()
medici_config.read(os.path.join(settings.BASE_DIR, 'medici_system/system/medici_config/medici.cfg'))

USER_USERNAME_PARAMETER = medici_config['Communication']['user_username_parameter']
USER_PASSWORD_PARAMETER = medici_config['Communication']['user_password_parameter']
USER_INFO_PARAMETER = medici_config['Communication']['user_info_parameter']

RECEIPT_IMAGE_PARAMETER = medici_config['Communication']['receipt_image_parameter']
RECEIPT_TEXT_PARAMETER = medici_config['Communication']['receipt_text_parameter']
RECEIPT_JSON_PARAMETER = medici_config['Communication']['receipt_json_parameter']

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

def receipt_image(request):
    check_post(request)
    mediciuser = check_auth(request)

    image = request.FILES[RECEIPT_IMAGE_PARAMETER]
    response = medici_system.receipt_image(mediciuser, image)

    return HttpResponse(response)

def receipt_text(request):
    check_post(request)
    mediciuser = check_auth(request)

    text = request.POST[RECEIPT_TEXT_PARAMETER]
    response = medici_system.receipt_text(mediciuser, text)

    return HttpResponse(response)

def receipt_json(request):
    check_post(request)
    mediciuser = check_auth(request)

    json = request.POST[RECEIPT_JSON_PARAMETER]
    response = medici_system.receipt_json(mediciuser, json)

    return HttpResponse(response)

def user_create(request):
    check_post(request)

    user_info = request.POST[USER_INFO_PARAMETER]
    response = medici_system.user_create(user_info)

    return HttpResponse(response)

def user_update(request):
    check_post(request)
    mediciuser = check_auth(request)

    user_info = request.POST[USER_INFO_PARAMETER]
    response = medici_system.user_update(mediciuser, user_info)

    return HttpResponse(response)

def user_last_updated(request):
    check_post(request)
    mediciuser = check_auth(request)

    response = medici_system.user_last_updated(mediciuser)

    return HttpResponse(response)

def user_fetch(request):
    check_post(request)
    mediciuser = check_auth(request)

    response = medici_system.user_fetch(mediciuser)

    return HttpResponse(response)

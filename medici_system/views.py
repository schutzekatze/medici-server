from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

import os
import json

from .system import medici_system

MEDICI_CONFIG = settings.MEDICI_CONFIG

USER_USERNAME_PARAMETER = MEDICI_CONFIG['communication']['user_username_param']
USER_PASSWORD_PARAMETER = MEDICI_CONFIG['communication']['user_password_param']
USER_DATA_PARAMETER = MEDICI_CONFIG['communication']['user_data_param']
USER_FIELDS_PARAMETER = MEDICI_CONFIG['communication']['user_fields_param']

RECEIPT_IMAGE_PARAMETER = MEDICI_CONFIG['communication']['receipt_image_param']
RECEIPT_TEXT_PARAMETER = MEDICI_CONFIG['communication']['receipt_text_param']
RECEIPT_DATA_PARAMETER = MEDICI_CONFIG['communication']['receipt_data_param']

def check_post(request):
    if request.method != 'POST':
        raise Http404

def check_auth(request):
    username = request.POST[USER_USERNAME_PARAMETER]
    password = request.POST[USER_PASSWORD_PARAMETER]
    user = authenticate(request, username=username, password=password)
    if user is None:
        raise PermissionDenied

    return user.mediciuser

@csrf_exempt
def user_create(request):
    check_post(request)

    user_data = json.loads(request.POST[USER_DATA_PARAMETER])
    response = medici_system.user_create(user_data)
    response = json.dumps(response)

    return HttpResponse(response)

@csrf_exempt
def user_update(request):
    check_post(request)
    mediciuser = check_auth(request)

    user_data = json.loads(request.POST[USER_DATA_PARAMETER])
    response = medici_system.user_update(mediciuser, user_data)
    response = json.dumps(response)

    return HttpResponse(response)

@csrf_exempt
def user_fetch(request):
    check_post(request)
    mediciuser = check_auth(request)

    user_fields = json.loads(request.POST[USER_FIELDS_PARAMETER])
    response = medici_system.user_fetch(mediciuser, user_fields)
    response = json.dumps(response)

    return HttpResponse(response)

@csrf_exempt
def receipt_image(request):
    check_post(request)
    mediciuser = check_auth(request)

    image = request.FILES[RECEIPT_IMAGE_PARAMETER].read()

    response = medici_system.receipt_image(mediciuser, image)
    response = json.dumps(response)

    return HttpResponse(response)

@csrf_exempt
def receipt_text(request):
    check_post(request)
    mediciuser = check_auth(request)

    text = json.loads(request.POST[RECEIPT_TEXT_PARAMETER])
    response = medici_system.receipt_text(mediciuser, text)
    response = json.dumps(response)

    return HttpResponse(response)

@csrf_exempt
def receipt_data(request):
    check_post(request)
    mediciuser = check_auth(request)

    data = json.loads(request.POST[RECEIPT_DATA_PARAMETER])
    response = medici_system.receipt_data(mediciuser, data)
    response = json.dumps(response)

    return HttpResponse(response)

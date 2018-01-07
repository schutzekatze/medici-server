from django.urls import path
from django.conf import settings

import os

from . import views

MEDICI_CONFIG = settings.MEDICI_CONFIG

USER_CREATE_URL = MEDICI_CONFIG['communication']['user_create_url']
USER_UPDATE_URL = MEDICI_CONFIG['communication']['user_update_url']
USER_FETCH_URL = MEDICI_CONFIG['communication']['user_fetch_url']

RECEIPT_IMAGE_URL = MEDICI_CONFIG['communication']['receipt_image_url']
RECEIPT_TEXT_URL = MEDICI_CONFIG['communication']['receipt_text_url']
RECEIPT_DATA_URL = MEDICI_CONFIG['communication']['receipt_data_url']

app_name = 'medici_system'
urlpatterns = [
    path(USER_CREATE_URL, views.user_create, name='user_create'),
    path(USER_UPDATE_URL, views.user_update, name='user_update'),
    path(USER_FETCH_URL, views.user_fetch, name='user_fetch'),
    path(RECEIPT_IMAGE_URL, views.receipt_image, name='receipt_image'),
    path(RECEIPT_TEXT_URL, views.receipt_text, name='receipt_text'),
    path(RECEIPT_DATA_URL, views.receipt_data, name='receipt_data'),
]

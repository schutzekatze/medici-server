from django.urls import path

from . import views

import os
import configparser
medici_config = configparser.ConfigParser()
medici_config.read(os.path.dirname(os.path.abspath(__file__)) + '/system/medici_config/medici.cfg')

MEDICI_SYSTEM_URL = medici_config['Communication']['medici_system_url']

RECEIPT_IMAGE_URL = medici_config['Communication']['receipt_image_url']
RECEIPT_TEXT_URL = medici_config['Communication']['receipt_text_url']
RECEIPT_JSON_URL = medici_config['Communication']['receipt_json_url']

USER_CREATE_URL = medici_config['Communication']['user_create_url']
USER_UPDATE_URL = medici_config['Communication']['user_update_url']
USER_LAST_UPDATED_URL = medici_config['Communication']['user_last_updated_url']
USER_FETCH_URL = medici_config['Communication']['user_fetch_url']

app_name = 'medici_system'
urlpatterns = [
    path(RECEIPT_IMAGE_URL, views.receipt_image, name='receipt_image'),
    path(RECEIPT_TEXT_URL, views.receipt_text, name='receipt_text'),
    path(RECEIPT_JSON_URL, views.receipt_json, name='receipt_json'),
    path(USER_CREATE_URL, views.user_create, name='user_create'),
    path(USER_UPDATE_URL, views.user_update, name='user_update'),
    path(USER_LAST_UPDATED_URL, views.user_last_updated, name='user_last_updated'),
    path(USER_FETCH_URL, views.user_fetch, name='user_fetch'),
]

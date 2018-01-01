from django.urls import path
from django.conf import settings

from . import views

import os
import configparser
medici_config = configparser.ConfigParser()
medici_config.read(os.path.join(settings.BASE_DIR, 'medici_system/system/medici_config/medici.cfg'))

USER_CREATE_URL = medici_config['Communication']['user_create_url']
USER_UPDATE_URL = medici_config['Communication']['user_update_url']
USER_FETCH_URL = medici_config['Communication']['user_fetch_url']

RECEIPT_IMAGE_URL = medici_config['Communication']['receipt_image_url']
RECEIPT_TEXT_URL = medici_config['Communication']['receipt_text_url']
RECEIPT_DATA_URL = medici_config['Communication']['receipt_data_url']

app_name = 'medici_system'
urlpatterns = [
    path(USER_CREATE_URL, views.user_create, name='user_create'),
    path(USER_UPDATE_URL, views.user_update, name='user_update'),
    path(USER_FETCH_URL, views.user_fetch, name='user_fetch'),
    path(RECEIPT_IMAGE_URL, views.receipt_image, name='receipt_image'),
    path(RECEIPT_TEXT_URL, views.receipt_text, name='receipt_text'),
    path(RECEIPT_DATA_URL, views.receipt_data, name='receipt_data'),
]

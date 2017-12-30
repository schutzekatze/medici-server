from django.urls import path

from . import views

app_name = 'medici_system'
urlpatterns = [
    path('receipt/image', views.receipt_image, name='receipt_image'),
    path('receipt/text', views.receipt_text, name='receipt_text'),
    path('receipt/json', views.receipt_json, name='receipt_json'),
    path('user/create', views.user_create, name='user_create'),
    path('user/update', views.user_update, name='user_update'),
    path('user/last_updated', views.user_last_updated, name='user_last_updated'),
    path('user/fetch', views.user_fetch, name='user_fetch'),
]

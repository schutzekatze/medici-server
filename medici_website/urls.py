from django.urls import path

from . import views

app_name = 'medici_website'
urlpatterns = [
    path('', views.index, name='index'),
]

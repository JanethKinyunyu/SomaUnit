from django.conf import settings
from django.urls import path
from . import views


app_name = 'Unit'

urlpatterns = [
    # path('', vi)
    path('', views.home, name='home' ),
]


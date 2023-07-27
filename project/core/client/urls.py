from django.urls import path

from core.client.views import *

app_name = 'client'

urlpatterns = [
    path('client/', ClientView.as_view(), name='client_view'),


]
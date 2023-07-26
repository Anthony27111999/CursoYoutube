from django.urls import path

from core.filtros.view import TestView

urlpatterns =[
    path('test/', TestView.as_view(),name='test')
]
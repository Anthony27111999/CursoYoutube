from django.urls import path

from core.dashboard.views import DashBoardView

urlpatterns =[
    path('', DashBoardView.as_view(), name='dashboard')
]
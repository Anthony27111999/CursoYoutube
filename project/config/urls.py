from django.contrib import admin
from django.urls import path, include

from core.homepage.views import IndexView
from core.login.views import LoginFormView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginFormView.as_view()),
    path('erp/', include('core.erp.urls')),
    path('', IndexView.as_view()),
]

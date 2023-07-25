from django.contrib import admin
from django.urls import path, include

from core.homepage.views import IndexView
from core.login.views import LoginFormView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', include('core.login.urls')),
    path('erp/', include('core.erp.urls')),
    path('dashboard/', include('core.dashboard.urls')),

]

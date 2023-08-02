from django.contrib import admin
from django.urls import path, include

from core.homepage.views import IndexView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', include('core.login.urls')),
    path('erp/', include('core.erp.urls')),
    path('erp/', include('core.product.urls')),
    path('dashboard/', include('core.dashboard.urls')),
    path('test/', include('core.filtros.urls')),
    path('client/', include('core.client.urls')),
    path('sale/', include('core.Sale.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import *

app_name = 'sale'

urlpatterns = [
    path('sale/list/', SaleListView.as_view(), name='sale_list'),
    path('sale/create/', SaleCreateView.as_view(), name='sale_create'),
    path('sale/update/<int:pk>/', SaleUpdateView.as_view(), name='sale_update'),
    path('sale/delete/<int:pk>/', SaleDeleteView.as_view(), name='sale_delete'),
    path('sale/invoice/pdf/<int:pk>', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf')
]
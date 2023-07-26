from django.urls import path
from core.product.views import *

app_name = 'product'

urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
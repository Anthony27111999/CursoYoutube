from django.urls import path

from core.erp.views import *

app_name = 'category'

urlpatterns = [
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

]
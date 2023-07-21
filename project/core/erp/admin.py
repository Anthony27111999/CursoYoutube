from django.contrib import admin

from core.erp.models import *

admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(DetSale)


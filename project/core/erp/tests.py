from  config.wsgi import *
from core.erp.models import Item, Employee
#
# Insert
CreateItem = Item()
CreateItem.name = 'ducto'
CreateItem.save()
#
# # Select de la tabla Item
# items = Item.objects.all()
# print(items)
#
# # Delete
# searchItem = Item.objects.get(id=1)
# searchItem.delete()
#
#  #Edit
#  try:
#      searchItem = Item.objects.get(id=1)
#      print(searchItem)
#   except Exception as e:
#      print(e)

# # Esto me busca cualquier dato que contengan esas letras
# consult = Item.objects.filter(name__icontains='du')
# # Esto me busca cualquier dato que empiezan con esas letras
# consult2 = Item.objects.filter(name__startswith='Du')
# # Esto me busca cualquier dato que terminan con esas letras
# consult3 = Item.objects.filter(name__endswith='o').exclude(name__contains='ducto')





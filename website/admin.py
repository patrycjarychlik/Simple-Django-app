from django.contrib import admin
from .models import List, Item, Budget, Service, Category

# Register your models here.

admin.site.register(List)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Budget)

from django.contrib import admin

from .models import Shop, Category, Product, Parameter, ProductParameter

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Parameter)
admin.site.register(ProductParameter)

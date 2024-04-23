from django.contrib import admin
from .models import Purchase, Registration, ProductImage

# Register your models here.
admin.site.register(Purchase)
admin.site.register(Registration)
admin.site.register(ProductImage)
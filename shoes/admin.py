from django.contrib import admin
from shoes import models

# Register your models here.

admin.site.register(models.Manufacturer)
admin.site.register(models.Shoe)
admin.site.register(models.ShoeColor)
admin.site.register(models.ShoeType)

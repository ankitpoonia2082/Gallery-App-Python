from django.contrib import admin

from .models import CategoryModel,ImageModel
# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(ImageModel)

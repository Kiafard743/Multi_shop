from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.Size)
admin.site.register(models.Color)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    prepopulated_fields = {'slug': ('title',)}
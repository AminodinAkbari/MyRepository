from django.contrib import admin
from .models import *
# Register your models here.
class ProductImageInline(admin.StackedInline):
    model = singleProductGallery

class ProductModelAdmin(admin.ModelAdmin):
    list_display    = ['title','available','image_tag']
    inlines         = [ProductImageInline]

class ColorsAdmin(admin.ModelAdmin):
    list_display = ['__str__','color_tag','code']

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Set)
admin.site.register(Tags)
admin.site.register(SingleProduct,ProductModelAdmin)
admin.site.register(Colors,ColorsAdmin)
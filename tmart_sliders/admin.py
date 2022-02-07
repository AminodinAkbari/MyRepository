from django.contrib import admin
from .models import *
# Register your models here.
class MainBigSliderModelAdmin(admin.ModelAdmin):
    list_display    = ['title','image_tag']

admin.site.register(MainBigSlider , MainBigSliderModelAdmin)
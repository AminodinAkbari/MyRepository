from django.contrib import admin
from .models import History
# Register your models here.
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product']

admin.site.register(History , HistoryAdmin)
from django.contrib import admin
from .models import *
# Register your models here.
class CouponAdmin(admin.ModelAdmin):
	list_display = ['code' , 'discount' , 'active']

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Favorite)
admin.site.register(Coupon , CouponAdmin)
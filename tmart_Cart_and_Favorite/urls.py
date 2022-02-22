from django.urls import path , include
from .views import add_to_order_detail
urlpatterns = [
	path('add_to_order_detail/<slug>' , add_to_order_detail)
]
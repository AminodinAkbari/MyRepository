from django.urls import path , include
from .views import *
urlpatterns = [
	path('add_to_order_detail/<slug>' , add_to_order_detail),
	path('Cart' , Cart_user),
	path('remove_item_fromcart/<order_id>',remove_item_fromcart),
]
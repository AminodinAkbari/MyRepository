from unicodedata import name
from django.urls import path , include
from .views import *
urlpatterns = [
	path('add_to_order_detail/<slug>' , add_to_order_detail , name = 'add_to_order_detail'),
	path('add_to_favorite/<slug>' , add_to_favorite , name = 'add_to_favorite'),
	path('Cart' , Cart_user,name = 'CartUser'),
	path('favorites' , FavoritePage.as_view()),
	path('delete_favorite/<order_id>' , remove_item_favorite),
	path('remove_item_fromcart/<order_id>',remove_item_fromcart),
]
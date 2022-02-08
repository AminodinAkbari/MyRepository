from django.urls import path , include
from .views import login_view, register
urlpatterns = [
	path('login' , login_view),
	path('register' , register),
]
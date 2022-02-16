from django.urls import path , include
from .views import login_view, register,logout_view
urlpatterns = [
	path('login' , login_view),
	path('register' , register),
	path('logout' , logout_view),
]
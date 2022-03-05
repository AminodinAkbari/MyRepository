from django.urls import path , include
from .views import login_view, register,logout_view
app_name = 'tmart_account'
urlpatterns = [
	path('login' , login_view , name = 'login'),
	path('register' , register),
	path('logout' , logout_view),
]
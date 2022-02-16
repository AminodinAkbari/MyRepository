from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm , RegisterForm
from django.contrib.auth.models import User
# Create your views here.

def login_view(request):
	if request.user.is_authenticated:
		return redirect('/')

	login_form = LoginForm(request.POST or None)
	if login_form.is_valid():
		username = login_form.cleaned_data.get('username')
		password = login_form.cleaned_data.get('password')
		user = authenticate(request ,username = username , password = password)
		if user is not None:
			login(request , user)
			return redirect('/')
		else:
			login_form.add_error('username','نام کاربری یا رمز عبور اشتباه است')
	return render(request , 'login.html' , {'login_form':login_form})


def register(request):
	register_form = RegisterForm(request.POST or None)
	if register_form.is_valid():
		username = register_form.cleaned_data.get('phone')
		password = register_form.cleaned_data.get('password')
		first_name = register_form.cleaned_data.get('first_name')
		last_name  = register_form.cleaned_data.get('last_name')
		User.objects.create_user(username = username , password = password , first_name = first_name , last_name = last_name)
		user = authenticate(username = username , password = password)
		if user is not None:
			login(request,user)
			return redirect('/')

	return render(request , 'register.html' , {'register_form':register_form})


def logout_view(request):
    logout(request)
    return redirect('/')
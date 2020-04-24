from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

User = get_user_model()

def old_home_page(request):
	html_= """ 
      sfafaasfasfsaf
      dsdfsdfsdfsd
      dssdsdd
      <h1>sdhhhdsf</h1>
	"""
	return HttpResponse(html_)

def home_page(request):
	context = {
	    "title" : "Hellow World!"
	}
	return render(request, "home.html", context)

def about_page(request):
	context = {
	    "title" : "About World!"
	}
	return render(request, "about.html", context)

def contact_page(request):
	form = ContactForm(request.POST or None)
	context = {
	    "title"    : "Contact World!",
	    "content"  : "Contact Page ",
	    "form"     :  form 
	}
	if form.is_valid():
		print('Valid')
		print(form.cleaned_data)	
	if request.method == 'POST':
		print(request.POST.get('name'))
		print(request.POST.get('email'))
		print(request.POST.get('message'))
		form = ContactForm()
	return render(request, "contact/view.html", context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
	    "title"    : "Login Page!",
	    "content"  : "Login Page ",
	    "form"     :  form 
	}
	print(request.user.is_authenticated)
	if form.is_valid() and request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			print('Loggin success')
			# Redirect to a success page.
		else:
		    print("Return an 'invalid login' error message.")
		form = LoginForm()
	return render(request, "auth/login.html", context)


def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
	    "title"    : "Register Page!",
	    "content"  : "User Registeration Page ",
	    "form"     :  form 
	}	
	if request.method == 'POST' and form.is_valid():
		username = request.POST.get('username')
		email    = request.POST.get('email')
		password = request.POST.get('password')
		new_user = User.objects.create_user(username, email, password)
		print(new_user)
		form = RegisterForm()
	return render(request, "auth/register.html", context)	







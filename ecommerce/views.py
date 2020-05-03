from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

User = get_user_model()



def about_view(request):
	context = { 'page_name': 'About'}
	return render(request, "about.html", context)

def home_view(request):
	context = { 'page_name': 'Home'}
	return render (request, "home.html", context)

def login_view(request):
	context = { 'page_name': 'Login'}
	return render (request, "login.html", context)

def blog_view(request):
    context = { 'page_name': 'Card List'}
    return render (request, "blog.html" , context)

def cart_view(request):
    context = { 'page_name': 'Card List'}
    return render (request, "cart.html" , context)

def category_view(request):
    context = { 'page_name': 'Product Catagory'}
    return render (request, "category.html" , context)

def confirmation_view(request):
    context = { 'page_name': 'Confirmation'}
    return render (request, "confirmation.html" , context)

def element_view(request):
    context = { 'page_name': 'Elements'}
    return render (request, "elements.html" , context)


def product_list_view(request):
    context = { 'page_name': 'Product List'}
    return render (request, "product_list.html" , context)

def product_detail_view(request):
    context = { 'page_name': 'Product Details'}
    return render (request, "product_detail.html" , context)

def blog_detail_view(request):
    context = { 'page_name': 'Blog Details'}
    return render (request, "blog_detail.html" , context)

def checkout_view(request):
    context = { 'page_name': 'Checkout'}
    return render (request, "checkout.html" , context)    

def contact_page(request):
	form = ContactForm(request.POST or None)
	context = {
	    "title"     : "Contact World!",
	    "content"   : "Contact Page ",
	    "page_name" : "Contact Us",
	    "form"      :  form 
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

def login_view(request):
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







from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Product
#from django.views.generic.detail import DetailView
from django.views.generic import ListView, DetailView

from django.utils import timezone
from django.http import Http404
# Create your views here.

# List Function 

# setup()
# dispatch()
# http_method_not_allowed()
# get_template_names()
# get_queryset()
# get_context_object_name()
# get_context_data()
# get()
# render_to_response()

class ProductFeaturedListView(ListView):
	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
	print("In details")
	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()

class ProductListView(ListView):
	#queryset      = Product.objects.all()
	#template_name = 'products/product_list.html'
	model      = Product
	paginate_by = 10

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		#print(context)
		return context

def product_list_view(request):
	queryset = Product.objects.all()
	context = { 'object_list':queryset }
	return render (request, "products/product_list.html", context)

class ProductDetailView(DetailView):
	#queryset = Product.objects.all()
	model      = Product
	#template_name = "products/product_detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		print("In get_context_data")
		return context

	# def get_queryset(self, *args, **kwargs):
	#     request = self.request
	#     pk      = self.kwargs.get('pk')
	#     print("In get_queryset")
	#     return Product.objects.filter(pk=pk)	


def product_detail_view(request, pk=None, *args, **kwargs):
	print(args)
	print(kwargs)

	#instance = Product.objects.filter(pk=pk)

	# try:
	# 	instanc = Product.objects.get(pk=pk)
	# except Product.DoesNotExiste:
	# 	raise Http404("Product doesn`t exist.")

	#instance = get_object_or_404(Product, pk=pk)
	#instance = get_list_or_404(Product, pk=pk)
	instance = Product.objects.get_by_id(pk)
	context  = { 'object' : instance }
	return render(request, "products/product_detail.html", context)







from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Create your views here.

class SearchProductView(ListView):
	""" Search Product by querystring"""
	template_name = 'search/view.html'
	#template_name = 'products/product_list.html'
	#model = Product
	def get_queryset(self, *args, **kwargs):
		request = self.request
		query   = request.GET.get('q')
		if query is not None:
			return Product.objects.filter(title__icontains =  query)
			'''
              __icontains = field contains this
              __iexact    = fields is exactly  this
			'''
		return Product.objects.none()	

"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import home_view, about_view, contact_page, login_view, register_page,\
blog_view, cart_view, category_view, confirmation_view,\
element_view, product_list_view, product_detail_view,\
blog_detail_view, checkout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('register/', register_page),
    path('', home_view),
    path('about/', about_view),
    path('blog/', blog_view),
    path('contact/', contact_page),
    path('cart/', cart_view),
    path('category/', category_view),
    path('confirmation/', confirmation_view),
    path('elements/', element_view),
    path('product-list/', product_list_view),
    path('product-detail/', product_detail_view),
    path('blog-detail/', blog_detail_view),
    path('checkout/', checkout_view),
    path('products/', include(('products.urls', 'products'), namespace="products")),
    path('search/', include(('search.urls', 'search'), namespace="search")), 
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

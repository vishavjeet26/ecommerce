from django.urls import path

from products.views import product_list_view, ProductListView \
,product_detail_view, ProductDetailView, ProductFeaturedListView, \
ProductFeaturedDetailView, ProductSlugDetailView, ProductHomeView, product_home_view


urlpatterns = [
    path('home/', product_home_view),
   # path('home/', ProductHomeView.as_view()),
    path('<int:pk>', ProductDetailView.as_view()),
    path('', ProductListView.as_view()),
    path('fbv/', product_list_view),
    path('fbv/<int:pk>', product_detail_view),
    path('<slug:slug>', ProductSlugDetailView.as_view(), name="detail"),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>', ProductFeaturedDetailView.as_view()),
    #path('product-fbv/<int:id>', product_detail_view),
]    
from django.urls import path
from tmart_Product.views import AllProducts,ProductSearch,product_detail
urlpatterns = [
    path('all_products' , AllProducts.as_view()),
    path('search' , ProductSearch.as_view()),
    path('product_details/<int:pk>' , product_detail),
]
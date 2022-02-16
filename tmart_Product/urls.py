from django.urls import path
from tmart_Product.views import AllProducts,ProductSearch,product_detail , SelectedSet
urlpatterns = [
    path('set/' , AllProducts.as_view() , name = 'AllProducts'),
    path('set/<int:id>' , SelectedSet.as_view() , name = 'set_with_id'),
    path('search' , ProductSearch.as_view() , name = 'search'),
    path('product_details/<slug>' , product_detail , name = 'product_details'),
]
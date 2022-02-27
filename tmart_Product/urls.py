from django.urls import path
from tmart_Product.views import (
    AllProducts,
    ProductSearch,
    SelectedSet,
    ProductDetail,
    test
)
urlpatterns = [
    path('set/' , AllProducts.as_view() , name = 'AllProducts'),
    path('set/<int:id>' , SelectedSet.as_view() , name = 'set_with_id'),
    path('search' , ProductSearch.as_view() , name = 'search'),
    path('ProductDetail/<slug>' , ProductDetail.as_view() , name = 'ProductDetail'),
    path('test' , test)
]
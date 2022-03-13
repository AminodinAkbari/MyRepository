from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

from .views import  Home
from Documentation.views import DocsList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view() , name = 'Home'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('docs/' , include('Documentation.urls')),
    path('', include('tmart_Product.urls')),
    path('', include('tmart_account.urls')),
    path('', include('tmart_settings.urls')),
    path('', include('tmart_Cart_and_Favorite.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

from .API_views import (
    SingleProductPriceRangeAPI,
    AllSingleProducts,
    SpecificSingleProducts,
    SingleProductsBySet,
    SingleProductsByColors,
    MostViewedSingleProducts
)
# REST-APIS
urlpatterns+=[
    path('product_price_range' , SingleProductPriceRangeAPI.as_view()),
    path('all_products' , AllSingleProducts.as_view()),
    path('all_products/<int:pk>' , SpecificSingleProducts.as_view()),
    path('single_products_by_set/<int:set_id>' , SingleProductsBySet.as_view()),
    path('single_products_by_colors/<color>' , SingleProductsByColors.as_view()),
    path('most_viewed_products' , MostViewedSingleProducts.as_view()),
]

if settings.DEBUG:
    urlpatterns=urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
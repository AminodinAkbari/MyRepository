from django.urls import path
from .views import DocsList

urlpatterns = [
	path('' , DocsList.as_view())
]
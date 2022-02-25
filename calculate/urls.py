from django.urls import path
from .views import calculate, getItemsByCategory

urlpatterns = [
	path('', calculate, name='home'),
	path('calculate/', calculate, name='calculate'),
	path('open-inventory/', getItemsByCategory, name='open_inventory'),
]
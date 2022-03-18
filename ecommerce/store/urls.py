from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('updateitem/', views.updateItem, name="update_item"),
	path('process_order/',views.processorder, name="process_order")
]
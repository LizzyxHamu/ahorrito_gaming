from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:producto_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:producto_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('decrement/<int:producto_id>/', views.decrement_cart_item, name='decrement_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/confirmation/', views.payment_confirmation, name='payment_confirmation'),
    path('order/success/', views.order_success, name='order_success'),
]
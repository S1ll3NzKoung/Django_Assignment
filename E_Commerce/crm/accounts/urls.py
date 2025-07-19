from django.urls import path
from . import views
from .views import * 

urlpatterns = [
    path('',views.index2,name='index2'),
    path('shop/',views.shop,name='shop'),
    path('shop_detail/',views.shop_detail,name='shop_detail'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('errors/',views.errors,name='errors'),
    path('contactE/', views.contactE, name='contactE'),
]
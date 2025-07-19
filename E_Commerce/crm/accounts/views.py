from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from rest_framework import generics 
# Create your views here.



def index2(request):
    Info = TblInfo.objects.all()
    Menu = TblMenu.objects.filter(id__in=[1,2,3,4,5]).distinct()
    menu_by_id = {item.id: item for item in Menu}
    SubMenu = TblSubMenu.objects.filter(SubMenuName__in=['Cart', 'Checkout', 'Testimonial', '404 Page']).distinct()
    
    context = {
        'Menu': menu_by_id,
        'SubMenu': SubMenu,
        'Info': Info
    }
    return render(request, 'E/index.html', context)

def shop(request):
    return render(request, 'E/shop.html')

def shop_detail(request):
    return render(request, 'E/shop-detail.html')

def cart(request):
    return render(request, 'E/cart.html')

def checkout(request):
    return render(request, 'E/checkout.html')

def testimonial(request):
    return render(request, 'E/testimonial.html')

def errors(request):
    return render(request, 'E/404.html')

def contactE(request):
    return render(request, 'E/contact.html')
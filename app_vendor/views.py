from django.shortcuts import render
from app_vendor.models import Product, Order, Store
from app_vendor.forms import ProductForm, OrderForm, StoreForm, OrderProductForm

def home(request):
    return render(request, "app_vendor/home.html")

def show_products(request):
    context = {
        "products": Product.objects.all(), 
    }
    return render(request, "app_vendor/product.html", context)

def add_product(request):
    if request.POST:
        product_form = ProductForm(request.POST)
        product_form.save()
    context = {
        "form": ProductForm(),
    }
    return render(request, "app_vendor/product_form.html", context)

def add_product_form(request):
    context = {
        "form": ProductForm()
    }

def show_orders(request):
    context = {
        "orders": Order.objects.all(), 
    }
    return render(request, "app_vendor/order.html", context)

def add_order(request):
    pass

def show_stores(request):
    pass

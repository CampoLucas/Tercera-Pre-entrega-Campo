from django.shortcuts import render
from vendor.models import Product, Order, Store
from vendor.forms import ProductForm, OrderForm, StoreForm

def home(request):
    return render(request, "vendor/home.html")

def show_products(request):
    context = {
        "products": Product.objects.all(), 
    }
    return render(request, "vendor/products.html", context)

def add_product(request):
    if request.POST:
        product_form = ProductForm(request.POST)
        product_form.save()
    context = {
        "form": ProductForm(),
    }
    return render(request, "vendor/product_form.html", context)

def show_orders(request):
    context = {
        "orders": Order.objects.all(), 
    }
    return render(request, "vendor/orders.html", context)

def add_order(request):
    if request.POST:
        order_form = OrderForm(request.POST)
        order_form.save()
    context = {
        "form": OrderForm(),
    }
    return render(request, "vendor/order_form.html", context)

def show_stores(request):
    context = {
        "stores": Store.objects.all(), 
    }
    return render(request, "vendor/stores.html", context)

def add_store(request):
    if request.POST:
        store_form = StoreForm(request.POST)
        store_form.save()
    context = {
        "form": StoreForm(),
    }
    return render(request, "vendor/store_form.html", context)

def search_product(request):
    criteria = request.GET.get("criteria")
    context = {
        'products': Product.objects.filter(name__icontains=criteria).all()
    }
    return render(request, "vendor/products.html", context)
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vendor.views import home, show_stores, show_orders, show_products, add_product, add_order, add_store, search_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('products', show_products, name='products'),
    path('products/add', add_product, name='add_product'),
    path('orders', show_orders, name='orders'),
    path('orders/add', add_order, name='add_order'),
    path('stores', show_stores, name='stores'),
    path('stores/add', add_store, name='add_store'),
    path('products/search', search_product, name='search_product')
]

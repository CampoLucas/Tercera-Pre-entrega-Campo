from django import forms
from vendor.models import Product, ProductOrder, Store

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = '__all__'

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
from django import forms
from vendor.models import Product, Order, Store

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Enter a description'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Enter a price', 'required': True}),
            'stock': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Enter stock', 'required': True}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
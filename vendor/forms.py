from django import forms
from vendor.models import Product, Order, Store

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Enter a description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Enter a price', 'required': True}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Enter stock', 'required': True}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'shiping_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter shipping address', 'required': True}),
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a product', 'required': True}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Enter stock', 'required': True}),
        }

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name', 'required': True}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter store location', 'required': True}),
        }
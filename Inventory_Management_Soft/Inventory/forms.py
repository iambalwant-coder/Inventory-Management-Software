from django import forms
from .models import Product, Order, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
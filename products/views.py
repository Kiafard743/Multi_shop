from django.shortcuts import render
from django.views.generic import DetailView

from products.models import Product


# Create your views here.
class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    model = Product

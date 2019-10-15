from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = ['article',
              'category', 
              'stock_qty',
              'unit_price',
              'short_description',
              'long_description',
              'main_image',
              'manufacturer',
              'ean',
              'weight',
              'weight_measure',
              'flavour',
              ]

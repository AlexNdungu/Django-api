from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics

# Create your views here.

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
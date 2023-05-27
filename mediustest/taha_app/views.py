from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from django.http import JsonResponse
# Create your views here.

# Products create view
class ProductsView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
# Products Edit, Delete View    
class ProductUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
    
    
# Products Image view
class ProductImageView(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    
# Variants create view
class VariantView(generics.ListCreateAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    
    

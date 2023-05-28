from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from django.http import JsonResponse
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

# Products create view
class ProductsView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    
# Search Filter by Title
class UserListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    
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
    
# Filter by variant    
class VariantFilterView(generics.ListAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
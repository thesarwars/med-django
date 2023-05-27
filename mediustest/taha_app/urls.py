from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', ProductsView.as_view()),
    path('update/<int:pk>', ProductUpdate.as_view()),
    path('product-image/', ProductImageView.as_view()),
    path('variant/', VariantView.as_view()),
]
 
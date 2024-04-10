from django.shortcuts import render
from rest_framework import viewsets
from .models import MyModel
from .serializers import ItemSerializer
from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = ItemSerializer

# def product_list(request):
#     products = Product.objects.all()  # Retrieve all products from the database
#     context = {'products': products}
#     return render(request, 'products/product_list.html', context)
    
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

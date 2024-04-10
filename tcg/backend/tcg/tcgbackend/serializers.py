from rest_framework import serializers
from .models import MyModel
from .models import Product

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Or list the fields you want to include
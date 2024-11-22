from rest_framework import serializers

from ..models.product import Product
from . import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True)

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "active",
            "category",
        ]

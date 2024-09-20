from products.models import Product
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    """Serializer for the Product model and its related data."""

    class Meta:
        model = Product
        fields = '__all__'

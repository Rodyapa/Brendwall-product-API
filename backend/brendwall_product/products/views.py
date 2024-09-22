from django.views.generic import ListView
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response


class ProductViewSet(viewsets.ViewSet):
    """
    View Set that process POST and GET API requests to products api endpoints.
    """
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndexView(ListView):
    model = Product
    template_name = 'index.html'

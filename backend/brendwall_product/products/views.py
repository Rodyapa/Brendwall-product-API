from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from products.models import Product
from products.forms import ProductForm
from products.serializers import ProductSerializer
from django.views.generic import ListView


class ProductAPIView(CreateModelMixin,
                     ListModelMixin,
                     GenericAPIView):
    """
    View that process POST and GET API requests to products api endpoints.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # ListModelMixin's list() for GET
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # CreateModelMixin's create() for POST
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class IndexView(ListView):
    model = Product
    template_name = 'index.html'
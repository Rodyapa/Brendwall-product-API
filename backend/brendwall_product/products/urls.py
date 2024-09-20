from django.urls import path, include
from products.views import IndexView
from products.views import ProductAPIView

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/products/', ProductAPIView.as_view(),
         name='product-list-create'),
]

from django.urls import path, include
from products.views import IndexView
from products.views import ProductAPIView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/products/add/', ProductAPIView.as_view(),
         name='product-create'),
    path('api/products/list', ProductAPIView.as_view(),
         name='product-list')
]
if settings.DEBUG is True:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from products.views import IndexView, ProductViewSet

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/products/list/',
         ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('api/products/add/',
         ProductViewSet.as_view({'post': 'create'}), name='product-create'),
]
if settings.DEBUG is True:
    urlpatterns + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Brendwall-product-API",
        default_version='v1',
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="rpadakov@yandex.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # I did not create a separate API
    # app because this project only requires one app.
    path('', include('products.urls')),
    path('api/schema/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api/schema.json/',
         schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
]


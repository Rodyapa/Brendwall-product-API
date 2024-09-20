from django.urls import path, include

urlpatterns = [
    # I did not create a separate API
    # app because this project only requires one app.
    path('', include('products.urls'))
]

from django.urls import path, include

urlpatterns = [
    path('cart/', include('api.cart.urls')),
    # path('users/', include('api.users.urls')),
]
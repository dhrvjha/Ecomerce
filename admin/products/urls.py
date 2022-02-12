"""
handle all the api request for products

"""


from django.urls import path
from .views import ProductViewSet


urlpatterns = [
    path('products/', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<uuid:pk>/', ProductViewSet.as_view({
        'get': 'retrive',
        'put': 'update',
        'delete': 'destroy'
    }))
]

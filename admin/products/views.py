from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Products
from .serializers import ProductSerializer

# Create your views here.


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, pk=None):
        try:
            product = Products.objects.get(uuid=pk)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Products.objects.get(uuid=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Products.objects.get(uuid=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

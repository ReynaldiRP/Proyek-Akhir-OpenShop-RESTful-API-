from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from backend_submission.serializers import ProductSerializer
from .models import Product


# Create your views here.
class ProductList(APIView):
    def get(self, request):
        """
        Retrieves all products.
        Supports search via query parameters, e.g., ?name=keyword&location=keyword
        """
        products = Product.objects.all()
        name = request.query_params.get('name', None)
        location = request.query_params.get('location', None)

        if name:
            products = products.filter(name__icontains=name)
        if location:
            products = products.filter(location__icontains=location)
        if not products:
            return Response({
                'products': [],
            }, status=status.HTTP_200_OK)

        serializers = ProductSerializer(products, many=True)

        return Response({
            'products': serializers.data,
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Creates a new product.
        """
        product = ProductSerializer(data=request.data, context={'request': request})
        if product.is_valid(raise_exception=True):
            product.save()
            return Response(product.data, status=status.HTTP_201_CREATED)

        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_object(self, pk):
        """
        Retrieves a product by its primary key.
        """
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieves a product by its primary key.
        """
        product = self.get_object(pk)
        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Updates a product by its primary key.
        """
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'message': 'Product updated successfully'
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Soft delete a product by setting is_delete to True.
        """
        product = self.get_object(pk)
        product.is_delete = True
        product.save()

        return Response({
            'message': 'Product deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)


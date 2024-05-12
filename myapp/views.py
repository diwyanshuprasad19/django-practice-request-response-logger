import logging
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductDetail
from .serializers import ProductDetailSerializer

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def product_detail_list(request):
    try:
        if request.method == 'GET':
            products = ProductDetail.objects.all()
            serializer = ProductDetailSerializer(products, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ProductDetailSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        logger.error(f"Error in product_detail_list view: {str(e)}")
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_detail(request, pk):
    try:
        product = ProductDetail.objects.get(pk=pk)
    except ProductDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        if request.method == 'GET':
            serializer = ProductDetailSerializer(product)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = ProductDetailSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        logger.error(f"Error in product_detail_detail view: {str(e)}")
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

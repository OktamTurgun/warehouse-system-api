from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductInputSerializer, ProductResultSerializer
from .services import calculate_materials

class CalculateMaterialsView(APIView):
  def post(self, request):
    # Input tekshirish
    input_serializer = ProductInputSerializer(data=request.data, many=True)
    if not input_serializer.is_valid():
      return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Product mavjudligini tekshirish
    for item in input_serializer.validated_data:
      if not Product.objects.filter(code=item['product_code']).exists():
        return Response({
          'error': f'Product with code {item['product_code']} not found'
        }, status=status.HTTP_404_NOT_FOUND)

    # Hisoblash
    result = calculate_materials(input_serializer.validated_data)

    # Output formatlash
    output_serializer = ProductResultSerializer(result, many=True)
    return Response({'result': output_serializer.data})
  
from rest_framework import serializers

class ProductMaterialOutputSerializer(serializers.Serializer):
  warehouse_id = serializers.IntegerField(allow_null=True)
  material_name = serializers.CharField()
  qty = serializers.FloatField()
  price = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)

class ProductResultSerializer(serializers.Serializer):
  product_name = serializers.CharField()
  product_qty = serializers.IntegerField()
  product_materials = ProductMaterialOutputSerializer(many=True)

class ProductInputSerializer(serializers.Serializer):
  product_code = serializers.IntegerField()
  quantity = serializers.IntegerField()

  
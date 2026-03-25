from django.contrib import admin
from .models import Product, Material, ProductMaterial, Warehouse

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'material', 'remainder', 'price']
    ordering = ['id']  # ID bo'yicha tartiblab ko'rsatadi

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'material', 'quantity']
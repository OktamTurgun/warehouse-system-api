from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)
  code = models.IntegerField(unique=True)

  def __str__(self):
    return self.name
  
class Material(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
class ProductMaterial(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  material = models.ForeignKey(Material, on_delete=models.CASCADE)
  quantity = models.FloatField()

  def __str__(self):
    return f"{self.product} - {self.material}"
  
class Warehouse(models.Model):
  material = models.ForeignKey(Material, on_delete=models.CASCADE)
  remainder = models.FloatField()
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"{self.material} - {self.remainder}"

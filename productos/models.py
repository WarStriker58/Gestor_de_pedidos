from django.db import models

class ProductCategory(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Product(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre
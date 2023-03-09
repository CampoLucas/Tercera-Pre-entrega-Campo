from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products', blank=True, null=True)

class ProductOrder(models.Model):
    shiping_address = models.TimeField()
    order_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='oredered_product')
    quantity = models.PositiveBigIntegerField()

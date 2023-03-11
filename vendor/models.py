from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()

class Order(models.Model):
    shiping_address = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    quantity = models.PositiveBigIntegerField()

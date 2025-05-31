import uuid

from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    shop = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    picture = models.CharField(max_length=500, blank=True, null=True)


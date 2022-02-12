from itertools import product
from django.db import models
import uuid

# Create your models here.


class Products(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=200, blank=True, editable=True)
    upc_ean_code = models.CharField(max_length=13, unique=True, null=True, blank=True)
    list_price = models.DecimalField(
        decimal_places=2, max_digits=9, null=True, blank=True
    )
    selling_price = models.CharField(max_length=200)
    quantity = models.IntegerField()
    model_number = models.CharField(max_length=200, null=True, blank=True)
    product_details = models.CharField(max_length=10000, null=True, blank=True)
    technical_details = models.CharField(max_length=10000, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    about_product = models.CharField(max_length=10000, null=True, blank=True)
    rating = models.DecimalField(decimal_places=2, max_digits=2, default=0.0)


class ProductImages(models.Model):
    image_url = models.URLField(null=False, blank=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

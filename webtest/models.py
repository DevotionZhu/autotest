from django.db import models
from product.models import Product
# Create your models here.
class Webcase(models.Model):
    Product = models.ForeignKey('product.Product',on_delete=models.CASCADE, null= True)
    webcasename = models.CharField('用例名称',max_length=200)

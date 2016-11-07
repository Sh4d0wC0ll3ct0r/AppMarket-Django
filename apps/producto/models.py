from django.db import models
from decimal import Decimal
from apps.Marca.models import Mark
# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price= models.DecimalField(max_digits=5,decimal_places=2)
    marks= models.ForeignKey(Mark,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
            return '{}'.format(self.name)

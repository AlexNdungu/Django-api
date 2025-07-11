from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.URLField(max_length=200)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

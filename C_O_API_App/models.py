from django.db import models

# Create your models here.
class Indexes(models.Model):
    symbolISIN = models.CharField(max_length = 250)
    variation = models.CharField(max_length = 250)
    top = models.CharField(max_length = 250)
    bottom = models.CharField(max_length = 250)
    opening_price = models.CharField(max_length = 250)

    def __str__(self):
        return self.symbolISIN
from django.db import models

# Create your models here.
class indexes(models.Model):
    symbolisin = models.CharField(max_length = 250)
    yesterday_variation = models.CharField(max_length = 250)
    asking_price = models.CharField(max_length = 250)
    biding_price = models.CharField(max_length = 250)
    opening_price = models.CharField(max_length = 250)

    def __str__(self):
        return self.symbolisin


class trigger(models.Model):
    user_symbol = models.CharField(max_length = 20)
    oper = models.IntegerField()
    desired_price = models.IntegerField()
    right_operand = models.CharField(max_length = 20)
    is_fired = models.BooleanField(default=True)

    def __str__(self):
        return self.user_symbol
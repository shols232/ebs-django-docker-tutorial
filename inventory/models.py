from django.db import models

class InventoryItem(models.Model):

    name = models.CharField(max_length=120)
    quantity = models.IntegerField(default=0)
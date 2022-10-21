from sre_constants import MAX_UNTIL
from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(
        max_length=48
    )
    destription = models.TextField(
        max_length=516
    )
    quantity = models.PositiveIntegerField()

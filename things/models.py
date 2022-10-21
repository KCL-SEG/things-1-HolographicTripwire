from sre_constants import MAX_UNTIL
from django.db import models

# Create your models here.
class Thing(models.Model):
    def __init__(self, name="", description="", quantity=1):
        self.name = name
        self.destription = description
        self.quantity = quantity
    """
    name = models.CharField(
        max_length=48
    )
    destription = models.CharField(
        max_length=516
    )
    quantity = models.PositiveIntegerField()
    """

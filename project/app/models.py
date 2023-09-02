from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class start(models.Model):
    name=models.CharField(max_length=255,null=False)
    age=models.IntegerField(null=False)

    class Meta:
        unique_together=["name","age"]

    def __str__(self):
        return f"{self.name}"
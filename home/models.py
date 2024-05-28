from django.db import models

# Create your models here.
class ProductType(models.Model):
    TypeID = models.AutoField(primary_key=True)
    TypeName = models.CharField(max_length=255)
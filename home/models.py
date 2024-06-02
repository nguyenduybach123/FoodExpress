from django.db import models

# Create your models here.
class ProductType(models.Model):
    TypeID = models.AutoField(primary_key=True)
    TypeName = models.CharField(max_length=255)

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Image = models.CharField(max_length=255)
    Rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    Sold = models.IntegerField()
    Describe = models.TextField()
    Discount = models.DecimalField(max_digits=5, decimal_places=2)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    TypeID = models.ForeignKey(ProductType, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

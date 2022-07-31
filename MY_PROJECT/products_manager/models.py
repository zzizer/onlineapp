from django.db import models

class Saler(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Saler, through='Product')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    saler_name = models.ForeignKey(Saler, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.CharField(max_length = 50000000)
        
    def __str__(self):
        return self.product_name
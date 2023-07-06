from django.db import models

class User(models.Model):
    username = models.TextField(max_length=100)
    password = models.TextField(max_length=50)


class Product(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='shop_image', blank=True)
    ram = models.IntegerField()
    color = models.TextField(max_length=50)
    memory = models.IntegerField()



class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Like(models.Model):
    like = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
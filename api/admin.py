from django.contrib import admin
from .models import User, Product, Order, Comment, Like

admin.site.register([
    User,
    Product,
    Order,
    Comment,
    Like,
])

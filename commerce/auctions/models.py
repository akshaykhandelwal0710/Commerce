from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length = 60)
    description = models.CharField(max_length = 500)
    opening = models.DecimalField(decimal_places = 2, max_digits = 10)
    image = models.URLField(default = "")
    sold = models.BooleanField(default = False)
    category = models.CharField(max_length = 60, default = None)
    date_created = models.DateTimeField()

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE)
    value = models.DecimalField(decimal_places = 2, max_digits = 10)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 500)
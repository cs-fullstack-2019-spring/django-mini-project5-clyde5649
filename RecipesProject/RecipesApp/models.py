from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RecipeModel(models.Model):
    meal = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(default='')
    recipecreator = models.CharField(max_length=20)
    imageURL = models.CharField(max_length=800, default="")


class UserModel(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    user_key = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
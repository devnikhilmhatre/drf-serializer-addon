from django.db import models

# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.CharField(max_length=100)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

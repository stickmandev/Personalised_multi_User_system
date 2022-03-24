from enum import unique
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bussinessName = models.CharField(unique=True, max_length=100, blank=False)
    logo = models.ImageField(upload_to=f'{bussinessName}s name', blank=True)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return self.bussinessName

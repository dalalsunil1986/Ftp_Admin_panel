import random
import string
from datetime import datetime
from django.db import models


"""Generate a random string of letters and digits """


def random_license_key(stringLength=20):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# Create your models here.


class Packages(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Tv(models.Model):
    name = models.CharField(max_length=200)
    number_of_channels = models.IntegerField
    price = models.IntegerField

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=50, blank=True)
    license_key = models.CharField(
        max_length=20, unique=True, default=random_license_key())
    domain = models.CharField(max_length=100)
    expire = models.DateTimeField(default=datetime.now, blank=False)
    join_date = models.DateTimeField(auto_now=True)
    package = models.ForeignKey(
        Packages, on_delete=models.SET_NULL, null=True, blank=True)
    tv_package = models.ForeignKey(
        Tv, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.first_name

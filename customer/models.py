from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class Customer(models.Model):  # Customer_Customer
    name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(22),MaxValueValidator(58)])
    email = models.EmailField(null=False,unique=True)
    joining_date = models.DateField()
    photo = models.ImageField(upload_to='resources/')
    balance = models.FloatField(default=0.0)


class Address(models.Model):  # Customer_Address
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()

    class Meta:
        db_table = "ADDRESS_INFO"
        ordering = ('pincode',)
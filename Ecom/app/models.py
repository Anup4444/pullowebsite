

from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sub_category(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default='', null=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=100, default='')
    image = models.ImageField(upload_to='prod/simg')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, default='')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=100, default='')
    image = models.ImageField(upload_to='prod/pimg')

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)


class Customer(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.username

    @staticmethod
    def get_customer_by_email(email):

        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

from django.contrib import admin
from .models import Product, Category, Sub_category, Customer
# Register your models here.


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'password']


@admin.register(Product)
class Adminproduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'image']


@admin.register(Category)
class Admincategory(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Sub_category)
class Adminsubcategory(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'category']

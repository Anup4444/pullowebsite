# Generated by Django 3.2.9 on 2022-06-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_customer_box'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='box',
            field=models.BooleanField(default=''),
        ),
    ]

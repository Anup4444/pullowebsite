# Generated by Django 3.2.9 on 2022-06-11 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='firstName',
            new_name='username',
        ),
    ]

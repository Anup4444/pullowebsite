# Generated by Django 3.2.9 on 2022-06-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='prod/fimg')),
            ],
        ),
    ]
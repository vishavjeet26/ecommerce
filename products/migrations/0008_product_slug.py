# Generated by Django 3.0.5 on 2020-04-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200429_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='abc'),
        ),
    ]

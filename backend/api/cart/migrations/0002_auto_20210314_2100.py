# Generated by Django 3.1.7 on 2021-03-14 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productrating',
            old_name='product_rating',
            new_name='product',
        ),
    ]
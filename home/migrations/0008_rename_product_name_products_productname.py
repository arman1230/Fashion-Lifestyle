# Generated by Django 4.0.1 on 2022-02-04 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_subcategories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_name',
            new_name='productname',
        ),
    ]
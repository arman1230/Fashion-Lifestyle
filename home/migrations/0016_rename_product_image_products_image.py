# Generated by Django 4.0.1 on 2022-02-08 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_products_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_image',
            new_name='image',
        ),
    ]

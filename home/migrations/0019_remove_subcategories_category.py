# Generated by Django 4.0.1 on 2022-02-08 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategories',
            name='category',
        ),
    ]
# Generated by Django 4.0.1 on 2022-03-07 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_shubimage_product_subimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('postal_code', models.CharField(max_length=30)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='shop/img')),
                ('product_desc', models.TextField(max_length=250)),
                ('product_quant', models.IntegerField()),
                ('publ_date', models.DateField()),
            ],
        ),
    ]
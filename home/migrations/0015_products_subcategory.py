# Generated by Django 4.0.1 on 2022-02-07 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_templates_imagename'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.subcategories'),
        ),
    ]

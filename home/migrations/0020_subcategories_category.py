# Generated by Django 4.0.1 on 2022-02-08 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_subcategories_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategories',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.categories'),
        ),
    ]

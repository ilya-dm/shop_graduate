# Generated by Django 2.2.10 on 2021-01-22 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210122_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='item',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]

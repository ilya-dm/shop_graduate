# Generated by Django 2.2.10 on 2021-01-22 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210122_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]

# Generated by Django 2.2.10 on 2021-02-09 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210201_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_items', to='shop.Product'),
        ),
    ]
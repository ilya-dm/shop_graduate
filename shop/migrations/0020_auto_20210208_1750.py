# Generated by Django 2.2.10 on 2021-02-08 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20210208_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 8, 17, 50, 52, 165938)),
        ),
    ]

# Generated by Django 2.2.10 on 2020-09-14 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='star',
            new_name='rating',
        ),
    ]
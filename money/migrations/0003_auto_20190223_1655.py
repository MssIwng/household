# Generated by Django 2.1.5 on 2019-02-23 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0002_auto_20190223_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='money',
            old_name='exchenge_date',
            new_name='exchange_date',
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0003_auto_20190223_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='exchange_date',
            field=models.DateTimeField(verbose_name='日付'),
        ),
    ]

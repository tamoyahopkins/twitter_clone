# Generated by Django 3.0.3 on 2020-03-03 03:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0011_auto_20200303_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.CharField(default=datetime.datetime(2020, 3, 3, 3, 18, 13, 610430, tzinfo=utc), max_length=200),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-02 19:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0005_auto_20200302_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.CharField(default=datetime.datetime(2020, 3, 2, 19, 34, 24, 456666, tzinfo=utc), max_length=200),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-02 20:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0008_auto_20200302_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='user_name',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.CharField(default=datetime.datetime(2020, 3, 2, 20, 46, 29, 899733, tzinfo=utc), max_length=200),
        ),
    ]

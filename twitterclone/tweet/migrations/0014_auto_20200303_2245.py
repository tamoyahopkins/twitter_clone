# Generated by Django 3.0.3 on 2020-03-03 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0013_auto_20200303_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

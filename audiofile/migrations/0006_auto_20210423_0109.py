# Generated by Django 3.2 on 2021-04-22 19:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('audiofile', '0005_auto_20210423_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='uploaded_time',
            field=models.DateField(default=datetime.datetime(2021, 4, 22, 19, 39, 18, 549999, tzinfo=utc), verbose_name='uploaded_time'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='uploaded_time',
            field=models.DateField(default=datetime.datetime(2021, 4, 22, 19, 39, 18, 547001, tzinfo=utc), verbose_name='Uploaded time'),
        ),
        migrations.AlterField(
            model_name='song',
            name='uploaded_time',
            field=models.DateField(default=datetime.datetime(2021, 4, 22, 19, 39, 18, 547001, tzinfo=utc), verbose_name='uploaded_time'),
        ),
    ]

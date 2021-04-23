# Generated by Django 3.2 on 2021-04-22 05:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('audiofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='uploaded_time',
            field=models.DateField(default=datetime.datetime(2021, 4, 22, 5, 42, 0, 734491, tzinfo=utc), verbose_name='uploaded_time'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='host',
            field=models.CharField(max_length=100, verbose_name='Host name'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='uploaded_time',
            field=models.DateField(default=datetime.datetime(2021, 4, 22, 5, 42, 0, 726497, tzinfo=utc), verbose_name='Uploaded time'),
        ),
        migrations.AlterField(
            model_name='song',
            name='uploaded_time',
            field=models.DateField(default=datetime.datetime(2021, 4, 22, 5, 42, 0, 726497, tzinfo=utc), verbose_name='uploaded_time'),
        ),
    ]
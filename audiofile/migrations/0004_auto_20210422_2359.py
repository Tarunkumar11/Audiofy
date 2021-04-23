# Generated by Django 3.2 on 2021-04-22 18:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('audiofile', '0003_auto_20210422_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='audiobook',
            name='duration',
            field=models.PositiveIntegerField(verbose_name='Audio Book duration'),
        ),
        migrations.AlterField(
            model_name='audiobook',
            name='uploaded_time',
            field=models.DateField(default=datetime.datetime(2021, 4, 22, 18, 29, 20, 683980, tzinfo=utc), verbose_name='uploaded_time'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='duration',
            field=models.PositiveIntegerField(verbose_name='Podcast duration'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='podcast_host', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='uploaded_time',
            field=models.DateField(default=datetime.datetime(2021, 4, 22, 18, 29, 20, 680982, tzinfo=utc), verbose_name='Uploaded time'),
        ),
        migrations.AlterField(
            model_name='song',
            name='uploaded_time',
            field=models.DateField(default=datetime.datetime(2021, 4, 22, 18, 29, 20, 679983, tzinfo=utc), verbose_name='uploaded_time'),
        ),
    ]

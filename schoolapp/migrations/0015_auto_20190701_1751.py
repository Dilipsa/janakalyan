# Generated by Django 2.2.2 on 2019-07-01 12:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0014_auto_20190701_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='total_day',
            new_name='total',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_schl_day',
        ),
        migrations.AddField(
            model_name='event',
            name='event',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='fr',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='from'),
            preserve_default=False,
        ),
    ]

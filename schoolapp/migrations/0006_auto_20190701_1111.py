# Generated by Django 2.2.2 on 2019-07-01 05:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0005_auto_20190701_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='to',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Shreepanchami Pooja'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='event_schl_day',
            field=models.DateTimeField(verbose_name='Annual School Day from'),
        ),
    ]

# Generated by Django 2.2.2 on 2019-07-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0013_exam_send_up'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='saraswati_pooja',
        ),
        migrations.AddField(
            model_name='event',
            name='total_day',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.2.2 on 2019-07-01 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0010_not_exams'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Not_carrier',
            new_name='Carrier',
        ),
        migrations.RenameModel(
            old_name='Not_event',
            new_name='Events',
        ),
        migrations.RenameModel(
            old_name='Not_exams',
            new_name='Exams',
        ),
    ]

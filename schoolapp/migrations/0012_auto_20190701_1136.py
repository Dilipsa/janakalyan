# Generated by Django 2.2.2 on 2019-07-01 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0011_auto_20190701_1134'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Exams',
            new_name='Exam',
        ),
    ]

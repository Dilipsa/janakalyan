# Generated by Django 2.2.2 on 2019-07-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0006_auto_20190701_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='to',
            field=models.DateTimeField(),
        ),
    ]

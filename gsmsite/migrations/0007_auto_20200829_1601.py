# Generated by Django 3.1 on 2020-08-29 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmsite', '0006_auto_20200829_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addevent',
            name='event_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

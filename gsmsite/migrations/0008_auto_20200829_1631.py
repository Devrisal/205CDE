# Generated by Django 3.1 on 2020-08-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmsite', '0007_auto_20200829_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addevent',
            name='event_date',
            field=models.DateTimeField(),
        ),
    ]
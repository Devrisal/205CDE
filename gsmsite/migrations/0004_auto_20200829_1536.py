# Generated by Django 3.1 on 2020-08-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmsite', '0003_auto_20200828_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addevent',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='addevent',
            name='event_image',
        ),
        migrations.AlterField(
            model_name='addpackage',
            name='package_image',
            field=models.FileField(upload_to=''),
        ),
    ]
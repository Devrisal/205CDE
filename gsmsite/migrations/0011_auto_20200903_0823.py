# Generated by Django 3.1 on 2020-09-03 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmsite', '0010_remove_addpackage_package_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addevent',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='addpackage',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

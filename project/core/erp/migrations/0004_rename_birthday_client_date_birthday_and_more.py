# Generated by Django 4.2.3 on 2023-07-28 03:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_category_date_creation_category_date_updated_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='birthday',
            new_name='date_birthday',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='sexo',
            new_name='gender',
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2023, 7, 28, 0, 53, 17, 391999)),
        ),
    ]

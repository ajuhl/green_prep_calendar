# Generated by Django 2.1.7 on 2019-03-30 22:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0011_auto_20190330_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 30, 22, 39, 32, 691805, tzinfo=utc)),
        ),
    ]

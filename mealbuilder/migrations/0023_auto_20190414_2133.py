# Generated by Django 2.1.7 on 2019-04-14 21:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0022_auto_20190331_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 21, 33, 4, 129806, tzinfo=utc)),
        ),
    ]

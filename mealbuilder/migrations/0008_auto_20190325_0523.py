# Generated by Django 2.1.7 on 2019-03-25 05:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0007_auto_20190325_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='calories',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='carbs',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 25, 5, 23, 16, 932812, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='meal',
            name='fat',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='fiber',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='protein',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]

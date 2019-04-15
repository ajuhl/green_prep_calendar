# Generated by Django 2.1.7 on 2019-03-31 05:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0019_auto_20190331_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='meal',
            name='carbs',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 31, 5, 40, 17, 785456, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='meal',
            name='fat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='fiber',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='protein',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mealitem',
            name='carbs',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mealitem',
            name='fat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mealitem',
            name='protein',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mealitem',
            name='quantity',
            field=models.FloatField(null=True),
        ),
    ]

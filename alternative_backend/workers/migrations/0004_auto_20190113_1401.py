# Generated by Django 2.1.4 on 2019-01-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_workerscan_day_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerscan',
            name='month',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workerscan',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
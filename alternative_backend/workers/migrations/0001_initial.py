# Generated by Django 2.1.4 on 2019-01-17 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('username', models.CharField(max_length=30)),
                ('barcode', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'workers',
            },
        ),
        migrations.CreateModel(
            name='WorkerScan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('week', models.IntegerField()),
                ('day_name', models.CharField(max_length=80)),
                ('seconds', models.BigIntegerField()),
                ('worker_barcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.Worker')),
            ],
            options={
                'db_table': 'worker_scan',
            },
        ),
    ]

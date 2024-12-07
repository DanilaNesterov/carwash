# Generated by Django 5.1.4 on 2024-12-07 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('discount', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('duration', models.PositiveIntegerField(default=30)),
            ],
        ),
        migrations.CreateModel(
            name='Washer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CarWashBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateTimeField()),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wash.box')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wash.client')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wash.service')),
                ('washer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wash.washer')),
            ],
        ),
    ]
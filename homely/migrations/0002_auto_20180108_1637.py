# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-08 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homely', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField(default=True)),
                ('availability_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='reservation_status',
            field=models.CharField(choices=[('Available', 'AVAILABLE'), ('Booked', 'BOOKED')], default='Available', max_length=100),
        ),
    ]
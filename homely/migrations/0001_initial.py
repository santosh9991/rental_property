# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-08 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeOwnerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyAllocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homely.HomeOwnerAccount')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('street_name', models.CharField(default='', max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_details', to='homely.HomeOwnerAccount')),
            ],
        ),
        migrations.CreateModel(
            name='RenterAccoount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('creation_ts', models.DateTimeField()),
                ('created_by_id', models.IntegerField(blank=True, null=True)),
                ('last_modification_ts', models.DateTimeField()),
                ('last_modified_by_id', models.IntegerField(blank=True, null=True)),
                ('is_active', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='propertydetails',
            unique_together=set([('created', 'city', 'state', 'zip_code')]),
        ),
    ]

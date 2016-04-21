# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ca', '0009_auto_20160325_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='revoked_reason',
            field=models.CharField(blank=True, choices=[('', 'No reason'), ('superseded', 'Superseded'), ('affiliationChanged', 'Affiliation changed'), ('cessationOfOperation', 'Cessation of operation'), ('unspecified', 'Unspecified'), ('certificateHold', 'On Hold'), ('keyCompromise', 'Key compromised'), ('CACompromise', 'CA compromised')], max_length=32, null=True, verbose_name='Reason for revokation'),
        ),
        migrations.AlterField(
            model_name='watcher',
            name='mail',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-Mail'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_sendgrid_parse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='to',
            new_name='to_mailbox',
        ),
        migrations.AddField(
            model_name='email',
            name='from_mailbox',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_conversation_message_message_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='thread_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

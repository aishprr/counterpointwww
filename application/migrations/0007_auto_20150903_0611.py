# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='venue',
            new_name='where',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='when',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='fblink',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='ticketlink',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]

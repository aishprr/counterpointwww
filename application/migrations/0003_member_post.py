# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_member_alumni'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='post',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]

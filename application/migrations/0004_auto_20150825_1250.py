# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_member_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='post',
            field=models.CharField(max_length=128),
        ),
    ]

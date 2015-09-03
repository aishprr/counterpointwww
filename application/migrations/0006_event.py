# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20150825_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('venue', models.CharField(max_length=128)),
                ('time', models.TimeField(max_length=128)),
                ('ticketlink', models.CharField(max_length=128)),
                ('fblink', models.CharField(max_length=128)),
            ],
        ),
    ]

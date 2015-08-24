# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('andrewid', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('part', models.CharField(max_length=128)),
                ('major', models.CharField(max_length=128)),
                ('graduation', models.IntegerField(default=0)),
                ('bio', models.CharField(max_length=2000)),
            ],
        ),
    ]

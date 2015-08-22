# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('culture_cal', '0003_auto_20150822_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='start_time',
            field=models.TimeField(),
        ),
    ]

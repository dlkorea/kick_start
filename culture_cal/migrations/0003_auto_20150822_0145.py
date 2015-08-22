# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('culture_cal', '0002_auto_20150822_0142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='end_date_time',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='start_date_time',
            new_name='start_time',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('langx', '0003_auto_20150822_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='level',
        ),
    ]

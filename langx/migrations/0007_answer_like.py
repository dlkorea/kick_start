# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('langx', '0006_auto_20150822_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]

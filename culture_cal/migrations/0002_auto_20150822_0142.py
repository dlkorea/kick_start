# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('culture_cal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='end_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 21, 16, 42, 3, 836095, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='start_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 21, 16, 42, 6, 726758, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='start_date',
            field=models.DateField(),
        ),
    ]

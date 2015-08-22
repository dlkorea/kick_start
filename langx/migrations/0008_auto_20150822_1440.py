# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('langx', '0007_answer_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(max_length=500),
        ),
    ]

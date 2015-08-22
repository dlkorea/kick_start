# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('langx', '0002_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ImageField(upload_to='langx/answer/%Y/%m/%d/', null=True, blank=True),
        ),
    ]

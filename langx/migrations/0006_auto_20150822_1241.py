# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('langx', '0005_auto_20150822_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mother_language',
            field=models.ForeignKey(null=True, related_name='mother_language_user', blank=True, to='langx.Language'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sub_language',
            field=models.ManyToManyField(null=True, related_name='sub_language_user', blank=True, to='langx.Language'),
        ),
    ]

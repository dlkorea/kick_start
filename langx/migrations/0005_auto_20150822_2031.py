# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('langx', '0004_auto_20150822_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='user/', default='/static/person.jpg'),
        ),
    ]

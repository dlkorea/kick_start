# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('langx', '0008_auto_20150822_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='like',
        ),
        migrations.AddField(
            model_name='answer',
            name='liked_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='liked_answer'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='user/', default='static/langx/images/person.jpg'),
        ),
    ]

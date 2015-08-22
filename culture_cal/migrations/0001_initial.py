# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import culture_cal.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('created_at', models.DateTimeField(verbose_name='작성일시', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='수정일시', auto_now=True)),
                ('hits', models.IntegerField(default=0, verbose_name='조회수')),
                ('next_reply_pk', models.IntegerField(default=0, verbose_name='댓글 번호')),
                ('image', models.ImageField(null=True, upload_to='calendar/%Y/%m/%d', blank=True)),
                ('author', models.ForeignKey(related_name='writed_article', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('liked_user', models.ManyToManyField(related_name='liked_article', verbose_name='추천인', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AttachedFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('attached_file', models.ImageField(default='', upload_to=culture_cal.utils.own_name_upload_to, blank=True, verbose_name='짤')),
                ('article', models.ForeignKey(to='culture_cal.Article')),
            ],
        ),
        migrations.CreateModel(
            name='AttachedImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('attached_image', models.FileField(default='', upload_to=culture_cal.utils.random_name_upload_to, blank=True, verbose_name='첨부파일')),
                ('article', models.ForeignKey(to='culture_cal.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('url_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('content', models.TextField(verbose_name='댓글내용')),
                ('created_at', models.DateTimeField(verbose_name='작성일시', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='수정일시', auto_now=True)),
                ('pk_related_to_article', models.IntegerField(default=0, verbose_name='댓글 번호')),
                ('article', models.ForeignKey(to='culture_cal.Article')),
                ('author', models.ForeignKey(related_name='writed_reply', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('liked_user', models.ManyToManyField(related_name='liked_reply', verbose_name='추천인', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='culture_cal.Tag'),
        ),
    ]

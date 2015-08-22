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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('hits', models.IntegerField(verbose_name='조회수', default=0)),
                ('next_reply_pk', models.IntegerField(verbose_name='댓글 번호', default=0)),
                ('image', models.ImageField(upload_to='calendar/%Y/%m/%d/')),
                ('author', models.ForeignKey(related_name='writed_article', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('liked_user', models.ManyToManyField(related_name='liked_article', to=settings.AUTH_USER_MODEL, verbose_name='추천인')),
            ],
        ),
        migrations.CreateModel(
            name='AttachedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('attached_file', models.ImageField(default='', verbose_name='짤', upload_to=culture_cal.utils.own_name_upload_to, blank=True)),
                ('article', models.ForeignKey(to='culture_cal.Article')),
            ],
        ),
        migrations.CreateModel(
            name='AttachedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('attached_image', models.FileField(default='', verbose_name='첨부파일', upload_to=culture_cal.utils.random_name_upload_to, blank=True)),
                ('article', models.ForeignKey(to='culture_cal.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('content', models.TextField(verbose_name='댓글내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('pk_related_to_article', models.IntegerField(verbose_name='댓글 번호', default=0)),
                ('article', models.ForeignKey(to='culture_cal.Article')),
                ('author', models.ForeignKey(related_name='writed_reply', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('liked_user', models.ManyToManyField(related_name='liked_reply', to=settings.AUTH_USER_MODEL, verbose_name='추천인')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='culture_cal.Tag'),
        ),
    ]

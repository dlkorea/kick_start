from django.db import models
from django.core.urlresolvers import reverse_lazy
from .utils import random_name_upload_to, own_name_upload_to
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    url_name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='제목')
    author = models.ForeignKey(User,
                               related_name="writed_article",
                               verbose_name='작성자')
    content = models.TextField(verbose_name='내용')
    tags = models.ManyToManyField('Tag')

    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일시')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일시')
    hits = models.IntegerField(default=0, verbose_name='조회수')
    liked_user = models.ManyToManyField(User,
                                        related_name="liked_article",
                                        verbose_name="추천인")

    next_reply_pk = models.IntegerField(default=0, verbose_name='댓글 번호')
    image = models.ImageField(upload_to='calendar/%Y/%m/%d',
                              blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy('calendar:view_article',
                            kwargs={
                                'article_number': self.id,
                            })

    def get_reply_pk(self):
        self.next_reply_pk += 1
        self.save()
        return self.next_reply_pk

    def get_page(self, rows_per_page):
        return self.calculate_page(self.id, rows_per_page)

    @classmethod
    def calculate_page(cls, id, rows_per_page):
        return cls.objects.filter(pk__gt=id).count() // rows_per_page + 1

    def hit_up(self):
        self.hits += 1
        self.save()
        return self.hits

    def count_reply(self):
        return self.next_reply_pk

    def like(self, user):
        self.liked_user.add(user)
        self.save()
        return self.count_like()

    def count_like(self):
        return self.liked_user.count()

    def is_action_done(self, user):
        return self.liked_user.filter(pk=user.id).exists()

    def save_tags(self, tag_list):
        for tag_name in tag_list:
            if Tag.objects.filter(name=tag_name).exists():
                tag = Tag.objects.get(name=tag_name)
                self.tags.add(tag)
            else:
                tag = Tag.objects.create(name=tag_name)
                self.tags.add(tag)
        self.save()
        return self.tags.all()

    def __str__(self):
        returnstr = ''.join([str(self.id), self.title,
                             '[', str(self.count_reply()), ']',
                             ' 조회 :', str(self.hits),
                             ' 좋아요 : ', str(self.count_like()),
                             ' 글쓴이 :', str(self.author)])
        return returnstr


class Reply(models.Model):
    content = models.TextField(verbose_name='댓글내용')
    author = models.ForeignKey(User,
                               related_name='writed_reply',
                               verbose_name='작성자')
    article = models.ForeignKey('Article')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일시')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일시')
    liked_user = models.ManyToManyField(User,
                                        related_name="liked_reply",
                                        verbose_name="추천인")
    pk_related_to_article = models.IntegerField(default=0,
                                                verbose_name='댓글 번호')

    def make_relation_with_article(self, article):
        self.article = article
        self.pk_related_to_article = article.get_reply_pk()
        return self.pk_related_to_article

    def count_like(self):
        return self.liked_user.count()

    def like(self, user):
        self.liked_user.add(user)
        self.save()
        return self.count_like()

    def is_action_done(self, user):
        return self.liked_user.filter(pk=user.id).exists()

    def __str__(self):
        return str(self.article) + '의 댓글 ' + str(self.id)


class AttachedImage(models.Model):
    article = models.ForeignKey('Article')
    attached_image = models.FileField(upload_to=random_name_upload_to,
                                      blank=True, default='',
                                      verbose_name='첨부파일')

    def __str__(self):
        return str(self.article) + '의 첨부 이미지, id: ' + str(self.id)


class AttachedFile(models.Model):
    article = models.ForeignKey('Article')
    attached_file = models.ImageField(upload_to=own_name_upload_to,
                                      blank=True, default='',
                                      verbose_name='짤')

    def __str__(self):
        return str(self.article) + '의 첨부 이미지, id: ' + str(self.id)


class Tag(models.Model):
    name = models.CharField(max_length=10)

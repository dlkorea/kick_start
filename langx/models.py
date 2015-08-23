from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from .utils import get_random_image


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    # level = models.ForeignKey('Level')
    # exp = models.IntegerField()
    mother_language = models.ForeignKey(
        'Language', related_name='mother_language_user', blank=True, null=True)
    sub_language = models.ManyToManyField(
        'Language', related_name='sub_language_user', blank=True, null=True)
    image = models.ImageField(upload_to='user/', default=get_random_image())


class Question(models.Model):
    # title = models.CharField(max_length=15)
    content = models.CharField(max_length=500)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    # image = models.ImageField(upload_to='langx/question/%Y/%m/%d/')
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.ForeignKey('Language')

    class Meta:
        ordering = ('-created_at', )

    def get_absolute_url(self):
        return reverse_lazy('langx:question_list', kwargs={
            'language_name': self.language})

    def __str__(self):
        return ''.join([self.content[:10], '...'])


class Answer(models.Model):
    question = models.ForeignKey('Question')
    content = models.TextField()
    liked_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_answer')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='langx/answer/%Y/%m/%d/',
                              blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def like(self, user):
        if user.is_authenticated():
            if not self.liked_user.filter(pk=user.pk).exists():
                self.liked_user.add(user)
                return True
            else:
                self.liked_user.remove(user)
                return True
        else:
            return 'fail'

    def __str__(self):
        return ''.join([self.content[:10], '...'])


class Tag(models.Model):
    tag_name = models.CharField(max_length=15)


class Level(models.Model):
    level = models.IntegerField()
    exp = models.IntegerField()
    icon = models.ImageField(upload_to='langx/lvl_icon/')


class Language(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

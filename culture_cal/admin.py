from django.contrib import admin
from .models import *


class ReplyInline(admin.StackedInline):
    model = Reply
    extra = 5


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'author', 'content',
                           'attached_images', 'attached_files']}),
    ]
    inlines = [ReplyInline]


admin.site.register(Reply)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

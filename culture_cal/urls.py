from django.conf.urls import url
from . import views

urlpatterns = [
    # 게시물 목록 보기
    url(r'^$', views.article_list, name="article_list"),


    # 게시물 작성, 검색
    url(r'^write/$', views.write_article, name="write_article"),
    url(r'^search/$', views.search_article, name="search_article"),

    # 게시물 보기, 추천, 수정, 삭제
    url(r'^(?P<article_number>\d+)/$',
        views.view_article, name="view_article"),
    url(r'^(?P<article_number>\d+)/like/$',
        views.like_article, name="like_article"),
    url(r'^(?P<article_number>\d+)/edit/$',
        views.edit_article, name="edit_article"),
    url(r'^(?P<article_number>\d+)/delete/$',
        views.delete_article, name="delete_article"),

    # 댓글 생성, 추천, 수정, 삭제
    url(r'^(?P<article_number>\d+)/comment/write/$',
        views.write_reply, name="write_reply"),
    url(r'^(?P<article_number>\d+)/comment/(?P<reply_number>\d+)/like/$',
        views.like_reply, name="like_reply"),
    url(r'^(?P<article_number>\d+)/comment/(?P<reply_number>\d+)/edit/$',
        views.edit_reply, name="edit_reply"),
    url(r'^(?P<article_number>\d+)/comment/(?P<reply_number>\d+)/delete/$',
        views.delete_reply, name="delete_reply"),
]

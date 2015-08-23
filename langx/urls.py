from django.conf.urls import url


urlpatterns = [

    url(r'logout', 'langx.views.logout', name='logout'),
    url(r'authenticate', 'langx.views.authenticate', name='authenticate'),
    url(r'create', 'langx.views.create', name='create'),

    url(r'^$', 'langx.views.index', name='index'),
    url(r'^like/(\d+)/$', 'langx.views.like', name='like'),

    url(r'^(?P<language_name>[a-zA-Z]+)/$', 'langx.views.question_list',
        name='question_list'),
    url(r'^(?P<language_name>[a-zA-Z]+)/search/$', 'langx.views.question_list',),
    url(r'^(?P<language_name>[a-zA-Z]+)/search/(?P<search_kw>[a-zA-Z0-9][^/\-_]+)/$',
        'langx.views.question_list'),
    url(r'^(?P<language_name>[a-zA-Z]+)/write/$', 'langx.views.write_question',
        name='write_question'),
    url(r'^question/(?P<question_id>\d+)/answer/write/$',
        'langx.views.write_answer', name='write_answer'),
]

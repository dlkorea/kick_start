from django.shortcuts import (render,
                              render_to_response,
                              redirect,
                              get_object_or_404,
                              )
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
# from django.contrib.auth.models import User

from .models import Article, Reply
from .forms import WriteArticle, WriteReply

# view_article에서도 사용함
rows_per_page = 20


def index(request):
    """
    if 'Windows' in request.META['HTTP_USER_AGENT']:
        return HttpResponse('Hello Computer')
    else:
        return HttpResponse('Hello SmartPhone')
    """
    return redirect(reverse_lazy('calendar:list_view'))


def list_by_period(request, date_str):
    if re.fullmatch(r('dddd'))
        date = date_str
    if date_str.count('-') == 1:
         =

    if day:

        article_in_period = Article.objects.filter(start_date__year=year,
                                                   start_date__month=month,
                                                   start_date__day=day,
                                                   end_date__year=year,
                                                   end_date__month=month,
                                                   end_date__day=day)
        article_over_period = article_in_period.filter(start_date__year=year,
                                                       start_date__month=month,
                                                       start_date__day=day,
                                                       end_date__year=year+1,
                                                       end_date__month=month+1,
                                                       end_date__day=day)
    params = {
        'article_in_period': article_in_period,
        'article_over_period': article_over_period,
    }
    return render(request, 'calendar/article_list_by.html', params)


def article_list(request):
    article_list = Article.objects.all()
    params = {
        'article_list': article_list,
    }
    return render(request, 'calendar/article_list.html', params)


# 게시물 보기
@login_required
def view_article(request, article_number):
    article = get_object_or_404(Article, pk=article_number)
    current_page = article.get_page(rows_per_page)
    params = {
        'article': article,
        'today': timezone.now(),
        'reply_form': WriteReply(),
        'current_page': current_page,
        'user': request.user,
    }
    article.hit_up()
    return render(request, 'calendar/view_article.html', params)


# 게시물 작성
@login_required
def write_article(request):
    if not request.user.is_staff:
        return render(request, 'calendar/no_permission.html')
    else:
        form = WriteArticle(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            tag_list = form.cleaned_data['tags']
            new_article.save_tags(tag_list)
            return redirect(new_article.get_absolute_url())
        params = {
            'form': form,
        }
        return render(request, 'calendar/write_article.html', params)


# 추천/비추천 둘다 여기서
@login_required
def like_article(request, article_number):
    if request.method == "POST":
        if request.is_ajax():
            article = Article.objects.get(pk=article_number)
            action = request.POST.get('action')
            if not article.is_action_done(request.user):
                if action == 'like':
                    article.like(request.user)
                elif action == 'dislike':
                    article.dislike(request.user)
                status = 'done'
            else:
                status = 'done_before'
            data = {
                'like': article.count_like(),
                'dislike': article.count_dislike(),
                'status': status,
            }
            return JsonResponse(data)
    else:
        return False


@login_required
def edit_article(request, article_number):
    article = get_object_or_404(Article, pk=article_number)
    form = WriteArticle(request.POST or None, request.FILES or None,
                        instance=article)
    if form.is_valid():
        article = form.save()
        tag_list = form.cleaned_data['tags']
        article.save_tags(tag_list)
        return redirect(article.get_absolute_url())
    params = {
        'form': form,
        'article': article,
    }
    return render(request, 'calendar/edit_article.html', params)


@login_required
def delete_article(request, article_number):
    article = get_object_or_404(Article, pk=article_number)
    article.delete()
    return redirect(reverse_lazy('calendar:article_list'))


def search_article(request):
    return HttpResponse('Not Yet Constructed')


@login_required
def write_reply(request, article_number):
    article = Article.objects.get(pk=article_number)
    reply_form = WriteReply(request.POST or None)
    if reply_form.is_valid():
        if not request.is_ajax():
            return HttpResponse("You need JavaScript!")
        else:
            reply = reply_form.save(commit=False)
            # reply manual pk 발급때문에 따로 처리
            reply.make_relation_with_article(article)
            reply.author = request.user
            reply.save()
            params = {
                'article': article,
                'today': timezone.now(),
                'user': request.user,
                'reply_form': WriteReply(),
            }
            return render(request, 'calendar/view_reply.html', params)
    else:
        error_msg = ''
        for key, value in reply_form.errors.items():
            error_msg += (key + ': ' + value + '<br/>')
        return HttpResponse(error_msg)
    return False


# 추천/비추천 둘다 여기서
@login_required
def like_reply(request, article_number, reply_number):
    if request.method == "POST":
        if request.is_ajax():
            reply = Reply.objects.get(pk=reply_number)
            action = request.POST.get('action')
            if not reply.is_action_done(request.user):
                if action == 'like':
                    reply.like(request.user)
                elif action == 'dislike':
                    reply.dislike(request.user)
                status = 'done'
            else:
                status = 'done_before'
            data = {
                'like': reply.count_like(),
                'dislike': reply.count_dislike(),
                'status': status,
            }
            return JsonResponse(data)
    else:
        return False


@login_required
def edit_reply(request, article_number, reply_number):
    reply = Reply.objects.get(pk=reply_number)
    form = WriteReply(request.POST or None, instance=reply)
    if form.is_valid():
        reply.save()
        return redirect(reply.article.get_absolute_url())
    params = {
        'reply_form': form,
        'reply': reply,
    }
    return render(request, 'calendar/edit_reply.html', params)


@login_required
def delete_reply(request, article_number, reply_number):
    reply = get_object_or_404(Reply, pk=reply_number)
    article = reply.article
    reply.delete()
    params = {
        'article': article,
        'replys': article.reply_set.all(),
        'reply_form': WriteReply(),
    }
    if request.is_ajax():
        return render(request, 'calendar/view_reply.html', params)
    return redirect(reply.article.get_absolute_url())


def request_view_ajax(request):
    if request.is_ajax():
        a = '<p> Yes aJax!! </p>'
    else:
        a = '<p> no aJax! </p>'

    a += '<h2>Headers</h2>'
    for key in request.META:
        a += '<p>'+str(key)+' : '+str(request.META.get(key)) + '</p>'
    a += '<br>'
    a += '<h2>Body</h2>'
    for key in request.POST:
        a += '<p>'+str(key)+' : '+str(request.POST.get(key)) + '</p>'
    return HttpResponse(a)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse_lazy
from .models import Question, Tag, Language, Answer
from .forms import QuestionForm, AnswerForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.context import RequestContext


def index(request):
    return render_to_response('langx/search.html',locals())


def like(request, pk):
    answer = Answer.objects.get(pk=pk)
    if request.is_ajax():
        return JsonResponse({
            'action': answer.like(request.user),
            'liked_user_number': answer.liked_user.count(),
        })
    else:
        return redirect(answer.question.get_absolute_url())


def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            next_url = 'langx:question_list'
            return redirect(next_url)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


# 로그인
@csrf_exempt
def authenticate(request):
    user = auth.authenticate(username=request.POST['username'],
                             password=request.POST['password'])
    if user is None:
        return HttpResponse('username or password error')
    auth.login(request, user)
    return HttpResponseRedirect('/langx/english/')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/langx/')


# 회원가입
@csrf_exempt
def create(request):
    try:
        user = User.objects.create_user(username=request.POST['username'],
                                        email=request.POST['email'],
                                        password=request.POST['password'])
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])
        auth.login(request, user)
        return HttpResponseRedirect('/langx/english/')
    except:
        return HttpResponse('실패, 이전 단계로 돌아가십시오')


def question_list(request, language_name, search_kw=None):
    language = Language.objects.get(name=language_name)
    if search_kw:
        question_list = language.question_set.filter(content__icontains=search_kw)
    else:
        question_list = language.question_set.all()
    params = {
        'question_list': question_list,
        'language_list': Language.objects.all(),
        'tag_list': Tag.objects.all(),
        'form': QuestionForm(),
        'answer_form': AnswerForm(),
        'search_kw': search_kw,
        'language': language,
    }
    return render(request, 'langx/question_list.html', params)


def write_question(request, language_name):
    form = QuestionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        new_question = form.save(commit=False)
        new_question.created_by = request.user
        new_question.language = Language.objects.get(name=language_name)
        new_question.save()
        if request.is_ajax():
            return render(request, 'langx/question.html', {
                'question': new_question,
                'answer_form': AnswerForm(),
            })
        else:
            return redirect(new_question.get_absolute_url())
    else:
        return HttpResponse('error')


def write_answer(request, question_id):
    form = AnswerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        new_answer = form.save(commit=False)
        new_answer.question = Question.objects.get(pk=question_id)
        new_answer.created_by = request.user
        new_answer.save()
        if request.is_ajax():
            return render(request, 'langx/answer.html', {
                'answer': new_answer,
            })
        else:
            return redirect(new_answer.question.get_absolute_url())
    else:
        question = Question.objects.get(pk=question_id)
        return redirect(question.get_absolute_url())

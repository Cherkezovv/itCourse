from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from posts.models import *
from answers.models import *

from .forms import QuestionsForm, DjangoQuestionsForm, HtmlCssQuestionsForm, JavaScriptQuestionsForm, \
    BootstrapQuestionsForm, NodejsQuestionsForm
from answers.views import *


def index(request):
    return render(request, 'posts/index.html')


def questions(request):
    questions = Questions.objects.order_by('-date_added')
    questions_p = Questions.objects.all()
    questions_d = DjangoQuestions.objects.order_by('-date_added')
    questions_d = DjangoQuestions.objects.all()
    return render(request, 'posts/questions.html', locals())


def question(request):
    question = Questions.objects.order_by('-date_added')
    question_p = Questions.objects.all()
    answer_p = PythonAnswers.objects.all()
    question_d = DjangoQuestions.objects.all()
    answer_d = DjangoAnswers.objects.all()
    question_h = HtmlCssQuestions.objects.all()
    answer_h = HtmlCssAnswers.objects.all()
    question_j = JavaScriptQuestions.objects.all()
    answer_j = JavaScriptAnswers.objects.all()
    question_b = BootstrapQuestions.objects.all()
    answer_b = BootstrapAnswers.objects.all()
    question_n = NodejsQuestions.objects.all()
    answer_n = NodejsAnswers.objects.all()
    return render(request, 'posts/ask/question.html', locals())


def new_questions(request):
    if request.method != 'POST':
        form = QuestionsForm()
    else:
        form = QuestionsForm(data=request.POST)
        if form.is_valid():
            new_questions = form.save(commit=False)
            new_questions.question = question
            new_questions.python_answers = question
            new_questions.save()
            return HttpResponseRedirect(reverse('question'))
    return render(request, 'posts/ask/new_questions.html', locals())


def django_question(request):
    d_question = DjangoQuestions.objects.order_by('date_added')
    question_d = DjangoQuestions.objects.all()
    answer_d = DjangoAnswers.objects.all()


def new_django_questions(request):
    if request.method != 'POST':
        form = DjangoQuestionsForm()
    else:
        form = DjangoQuestionsForm(data=request.POST)
        if form.is_valid():
            new_django_questions = form.save(commit=False)
            new_django_questions.django_question = django_question
            new_django_questions.save()
            return HttpResponseRedirect(reverse('question'))
    return render(request, 'posts/ask/new_django_questions.html', locals())


def htmlcss_question(request):
    question_h = HtmlCssQuestions.objects.all()
    answer_h = HtmlCssAnswers.objects.all()


def new_htmlcss_questions(request):
    if request.method != 'POST':
        form = HtmlCssQuestionsForm()
    else:
        form = HtmlCssQuestionsForm(data=request.POST)
        if form.is_valid():
            new_htmlcss_questions = form.save(commit=False)
            new_htmlcss_questions.htmlcss_question = htmlcss_question
            new_htmlcss_questions.save()
            return HttpResponseRedirect(reverse('question'))
    return render(request, 'posts/ask/new_htmlcss_questions.html', locals())


def javascript_question(request):
    question_j = JavaScriptQuestions.objects.all()
    answer_j = JavaScriptAnswers.objects.all()


def new_javascript_questions(request):
    if request.method != 'POST':
        form = JavaScriptQuestionsForm()
    else:
        form = JavaScriptQuestionsForm(data=request.POST)
        if form.is_valid():
            new_javascript_questions = form.save(commit=False)
            new_javascript_questions.javascript_question = javascript_question
            new_javascript_questions.save()
            return HttpResponseRedirect(reverse('question'))
    return render(request, 'posts/ask/new_javascript_questions.html', locals())


def bootstrap_question(request):
    question_b = BootstrapQuestions.objects.all()
    answer_b = BootstrapAnswers.objects.all()


def new_bootstrap_questions(request):
    if request.method != 'POST':
        form = BootstrapQuestionsForm()
    else:
        form = BootstrapQuestionsForm(data=request.POST)
        if form.is_valid():
            new_bootstrap_questions = form.save(commit=False)
            new_bootstrap_questions.bootstrap_question = bootstrap_question
            new_bootstrap_questions.save()
            return HttpResponseRedirect(reverse('question'))
    return render(request, 'posts/ask/new_bootstrap_questions.html', locals())


def nodejs_question(request):
    question_n = NodejsQuestions.objects.all()
    answer_n = NodejsAnswers.objects.all()


def new_nodejs_questions(request):
    if request.method != 'POST':
        form = NodejsQuestionsForm()
    else:
        form = NodejsQuestionsForm(data=request.POST)
        if form.is_valid():
            new_nodejs_questions = form.save(commit=False)
            new_nodejs_questions.nodejs_question = nodejs_question
            new_nodejs_questions.save()
            return HttpResponseRedirect(reverse('question'))
    return render(request, 'posts/ask/new_nodejs_questions.html', locals())


def tasks(request):
    return render(request, 'posts/tasks.html')


def about(request):
    return render(request, 'posts/about.html')


def blog(request):
    return render(request, 'posts/blog.html')


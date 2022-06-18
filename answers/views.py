from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from answers.models import *
from posts.views import *
from .forms import *


def python_answer(request, question_id):
    python_answer = Questions.objects.get(id=question_id)
    ans = python_answer.pythonanswers_set.order_by('-date_added')
    answer_p = PythonAnswers.objects.all()
    question = Questions.objects.all()
    if request.method != 'POST':
        form = PythonAnswersForm()
    else:
        form = PythonAnswersForm(data=request.POST)
        if form.is_valid():
            new_python_answers = form.save(commit=False)
            new_python_answers.question = python_answer
            new_python_answers.save()
            counts = new_python_answers.question
            
            
            for i in str(counts):
                ttt=0;
                ttt=ttt+1;
                print(ttt,' ',i)
            print(counts)
            return HttpResponseRedirect(reverse('python_answer', args=[question_id]))
    return render(request, 'posts/answers/python_answer.html', locals())


def django_answer(request, django_question_id):
    django_answer = DjangoQuestions.objects.get(id=django_question_id)
    ans_d = django_answer.djangoanswers_set.order_by('-date_added')
    if request.method != 'POST':
        form = DjangoAnswersForm()
    else:
        form = DjangoAnswersForm(data=request.POST)
        if form.is_valid():
            new_django_answers = form.save(commit=False)
            new_django_answers.django_question = django_answer
            new_django_answers.save()
            return HttpResponseRedirect(reverse('django_answer', args=[django_question_id]))
    return render(request, 'posts/answers/django_answer.html', locals())


def htmlcss_answer(request, htmlcss_question_id):
    htmlcss_answer = HtmlCssQuestions.objects.get(id=htmlcss_question_id)
    ans_h = htmlcss_answer.htmlcssanswers_set.order_by('-date_added')
    if request.method != 'POST':
        form = HtmlCssAnswersForm()
    else:
        form = HtmlCssAnswersForm(data=request.POST)
        if form.is_valid():
            new_htmlcss_answers = form.save(commit=False)
            new_htmlcss_answers.htmlcss_question = htmlcss_answer
            new_htmlcss_answers.save()
            return HttpResponseRedirect(reverse('htmlcss_answer', args=[htmlcss_question_id]))
    return render(request, 'posts/answers/htmlcss_answer.html', locals())


def javascript_answer(request, javascript_question_id):
    javascript_answer = JavaScriptQuestions.objects.get(id=javascript_question_id)
    ans_j = javascript_answer.javascriptanswers_set.order_by('-date_added')
    answer_j = JavaScriptAnswers.objects.all()
    if request.method != 'POST':
        form = JavaScriptAnswersForm()
    else:
        form = JavaScriptAnswersForm(data=request.POST)
        if form.is_valid():
            new_javascript_answers = form.save(commit=False)
            new_javascript_answers.javascript_question = javascript_answer
            new_javascript_answers.save()
            return HttpResponseRedirect(reverse('javascript_answer', args=[javascript_question_id]))
    return render(request, 'posts/answers/javascript_answer.html', locals())


def bootstrap_answer(request, bootstrap_question_id):
    bootstrap_answer = BootstrapQuestions.objects.get(id=bootstrap_question_id)
    ans_b = bootstrap_answer.bootstrapanswers_set.order_by('-date_added')
    answer_b = BootstrapAnswers.objects.all()
    bootstrap_answer = BootstrapQuestions.objects.get(id=bootstrap_question_id)
    if request.method != 'POST':
        form = BootstrapAnswersForm()
    else:
        form = BootstrapAnswersForm(data=request.POST)
        if form.is_valid():
            new_bootstrap_answers = form.save(commit=False)
            new_bootstrap_answers.bootstrap_question = bootstrap_answer
            new_bootstrap_answers.save()
            return HttpResponseRedirect(reverse('bootstrap_answer', args=[bootstrap_question_id]))
    return render(request, 'posts/answers/bootstrap_answer.html', locals())


def nodejs_answer(request, nodejs_question_id):
    nodejs_answer = NodejsQuestions.objects.get(id=nodejs_question_id)
    ans_n = nodejs_answer.nodejsanswers_set.order_by('-date_added')
    answer_n = NodejsAnswers.objects.all()
    nodejs_answer = NodejsQuestions.objects.get(id=nodejs_question_id)
    if request.method != 'POST':
        form = NodejsAnswersForm()
    else:
        form = NodejsAnswersForm(data=request.POST)
        if form.is_valid():
            new_nodejs_answers = form.save(commit=False)
            new_nodejs_answers.nodejs_question = nodejs_answer
            new_nodejs_answers.save()
            return HttpResponseRedirect(reverse('nodejs_answer', args=[nodejs_question_id]))
    return render(request, 'posts/answers/nodejs_answer.html', locals())

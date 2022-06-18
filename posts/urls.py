from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.questions, name='questions'),

    path('question/', views.question, name='question'),
    path('new_questions/', views.new_questions, name='new_questions'),

    path('django_question/', views.django_question, name='django_question'),
    path('new_django_questions/', views.new_django_questions, name='new_django_questions'),

    path('htmlcss_question/', views.htmlcss_question, name='htmlcss_question'),
    path('new_htmlcss_questions/', views.new_htmlcss_questions, name='new_htmlcss_questions'),

    path('javascript_question/', views.javascript_question, name='javascript_question'),
    path('new_javascript_questions/', views.new_javascript_questions, name='new_javascript_questions'),

    path('bootstrap_question/', views.bootstrap_question, name='bootstrap_question'),
    path('new_bootstrap_questions/', views.new_bootstrap_questions, name='new_bootstrap_questions'),

    path('nodejs_question/', views.nodejs_question, name='nodejs_question'),
    path('new_nodejs_questions/', views.new_nodejs_questions, name='new_nodejs_questions'),

    path('tasks/', views.tasks, name='tasks'),
    path('about/', views.about, name='about'),
    path('our_blog/', views.blog, name='blog'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('python_answer/<int:question_id>', views.python_answer, name='python_answer'),
    path('django_answer/<int:django_question_id>', views.django_answer, name='django_answer'),
    path('htmlcss_answer/<int:htmlcss_question_id>', views.htmlcss_answer, name='htmlcss_answer'),
    path('javascript_answer/<int:javascript_question_id>', views.javascript_answer, name='javascript_answer'),
    path('bootstrap_answer/<int:bootstrap_question_id>', views.bootstrap_answer, name='bootstrap_answer'),
    path('nodejs_answer/<int:nodejs_question_id>', views.nodejs_answer, name='nodejs_answer'),

]

from email import header
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from message.forms import MessagesForm
# from django.conf import settings
# from question_task.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .models import Messages

def contact_view(request):
    
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = MessagesForm()
    
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = MessagesForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(from_email, message,
                          from_email,['webprogcoder@gmail.com'], fail_silently=False)
               
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "message/contact.html", {'form': form})

def success_view(request):
    return render(request, "message/success.html")
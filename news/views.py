from django.shortcuts import render
from news.models import News


def news(request):
    newss = News.objects.order_by('-date_added')
    return render(request, 'news.html', locals())

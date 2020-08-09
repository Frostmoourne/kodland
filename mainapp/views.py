from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .forms import NewArticle
from .models import Articles


def main(request, pk=None):
    title = 'главная'
    main_article = Articles.objects.order_by('-upload')[:1]
    other_articles_1 = Articles.objects.order_by('-upload').all()[1:4]
    other_articles_2 = Articles.objects.order_by('-upload').all()[4:7]
    other_articles_3 = Articles.objects.order_by('-upload').all()[7:10]
    content = {
        'title': title,
        'main_article': main_article,
        'other_articles_1': other_articles_1,
        'other_articles_2': other_articles_2,
        'other_articles_3': other_articles_3,
    }
    return render(request, 'mainapp/index.html', content)


def article(request, pk=None):
    title = 'статья'
    data = Articles.objects.filter(pk=pk)
    content = {
        'title': title,
        'data': data,
    }
    return render(request, 'mainapp/article.html', content)


def add(request):
    title = 'опубликовать'
    if request.method == 'POST':
        article_form = NewArticle(request.POST, request.FILES)
        article_form.save()
        return HttpResponseRedirect(reverse('articles:index'))
    else:
        article_form = NewArticle()
    content = {
        'title': title,
        'article_form': article_form,
    }
    return render(request, 'mainapp/add.html', content)
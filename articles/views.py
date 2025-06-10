from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by('created_at')
    return render(request, 'articles/article_list.html', {'articles': articles})  

def article_detail(request, slug): 
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = forms.createArticle(request.POST, request.FILES)
        if form.is_valid():
            thisArticle = form.save(commit=False)
            thisArticle.author = request.user
            thisArticle.save()
            return redirect('articles:article_list')
    else:
        form = forms.createArticle()
    return render(request, 'articles/article_create.html', {'form': form})
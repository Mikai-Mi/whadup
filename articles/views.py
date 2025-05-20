from django.shortcuts import render
from .models import Article
#from django.shortcuts import get_object_or_404

def article_list(request):
    articles = Article.objects.all().order_by('created_at')
    return render(request, 'articles/article_list.html', {'articles': articles})  


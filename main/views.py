from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CommentForm
from .models import *


def home(request):
    return render(request, 'main/dashboard.html')

def researches(request):
    return render(request, 'main/researches.html')

def research(request):
    return render(request, 'main/research.html')

def resume(request):
    return render(request, 'main/resume.html')

def projects(request):
    return render(request, 'main/projects.html')

def articles(request):
    articles = Article.objects.filter(Q(type='Article'))
    context = {'articles' : articles}
    return render(request, 'main/articles.html', context)

def article(request, title):
    article = get_object_or_404(Article, title=title)
    comments = Comment.objects.filter(article=article)
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article', title=article.title)
    else:
        initial_data = {'title': article.title}
        comment= CommentForm(initial=initial_data)
    context = {'article': article, 'comment': comment}
    return render(request, 'main/article.html', context)

def stories(request):
    stories = Article.objects.filter(Q(type='Story'))
    context = {'stories' : stories}
    return render(request, 'main/stories.html', context)

def story(request, title):
    article = get_object_or_404(Article, title=title)
    comments = Comment.objects.filter(article=article)
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('story', title=article.title)
    else:
        initial_data = {'title': article.title}
        comment= CommentForm(initial=initial_data)
    context = {'story': article, 'comment': comment}
    return render(request, 'main/story.html', context)

def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('article', title=comment.article.title)
    else:
        comment_form = CommentForm(instance=comment)
    context = {'comment': comment, 'comment_form': comment_form}
    return render(request, 'main/update_comment.html', context)

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('article', title=comment.article.title)
    context = {'comment': comment}
    return render(request, 'main/delete_comment.html', context)

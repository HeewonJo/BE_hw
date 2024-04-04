from django.shortcuts import render
from .models import Post
from django.db.models import Q 

def list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "posts/list.html", {'posts' : posts})

def result(request):
    word = request.GET['word']
    words = Post.objects.filter(Q(title__contains = word) | Q(content__contains = word)).order_by('-created_at')
    return render(request, "posts/result.html", {'word' : word, 'posts' : words})
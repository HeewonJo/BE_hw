from django.shortcuts import render
from .models import Post
from django.db.models import Q

def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/list.html', {'posts' : posts})
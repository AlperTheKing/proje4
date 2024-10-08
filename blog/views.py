from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'blog_posts': blog_posts})

def blog_detail(request, id):
    blog_post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/blog_detail.html', {'blog_post': blog_post})
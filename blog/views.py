from django.shortcuts import render,  get_object_or_404
from .models import *

# Create your views here.

def home_view(request):
    template_url = 'blog/index.html'
    blog = Blog.objects.all().first()
    featured_post = Post.objects.all().filter(featured=True)[:4]
    story_post = Post.objects.all().filter(featured=False)
    related_post_url = Post.objects.all()[:3]
    context = {'blog':blog, 'featured_post': featured_post, 'story_post': story_post, 'related_post_url': related_post_url}
    return render(request, template_url, context)

def single_view(request, slug):
    teplate_url = 'blog/post.html'
    posts = get_object_or_404(Post, slug=slug)
    related_post = Post.objects.all()[:3]
    context = {'posts': posts, 'related_post': related_post}
    return render(request, teplate_url, context)

# def related_view(request):
#     template_url = 'blog/post.html'
#     related_post_view = Post.objects.all()[:3]
#     context = {'related_post_view':related_post_view}
#     return render(request, template_url, context)

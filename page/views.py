from blog.models import Blog
from django.shortcuts import render


def home_view(request):
    posts = Blog.objects.filter(is_active=True).order_by('-created_at')
    context = {
        'posts': posts

    }
    return render(request, 'index.html', context)

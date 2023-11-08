from blog.models import Blog, BlogCategory, BlogTag
from django.shortcuts import render


def home_view(request):
    posts = Blog.objects.filter(is_active=True)
    top_posts = posts.order_by('-view_count')[:6]
    categories = BlogCategory.objects.filter(is_active=True)
    tags = BlogTag.objects.filter(is_active=True)
    context = {
        'posts': posts,
        'top_posts': top_posts,
        'categories': categories,
        'tags': tags,

    }
    return render(request, 'index.html', context)

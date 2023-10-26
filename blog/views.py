from django.shortcuts import render
from .models import Blog, BlogCategory, BlogTag
from .forms import BlogModelForm


def create_blog_view(request):
    form = BlogModelForm()
    context = {
        'form': form,
    }
    return render(request, 'create_blog.html', context)

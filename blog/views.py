from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

import json

from .models import Blog, BlogCategory, BlogTag
from .forms import BlogModelForm


@login_required(login_url='user_profile:login_view')
def create_blog_view(request):
    form = BlogModelForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        # to get media files we should add request.FILES or None
        form = BlogModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            # form object created by save method
            f.save()
            tags_data = json.loads(form.cleaned_data.get('tag'))
            for tag_data in tags_data:
                tag, created = BlogTag.objects.get_or_create(title=tag_data.get('value').lower())
                # after we changed value of object we should save it
                tag.is_active = True
                tag.save()
                # save new tags to db
                f.tag.add(tag)
            messages.success(request, 'Blog created successfully')
            return redirect('home_view')

    return render(request, 'create_blog.html', context)


def category_view(request, category_slug):
    category = get_object_or_404(BlogCategory, slug=category_slug)
    posts = Blog.objects.filter(category=category)
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'components/post_list.html', context)


def tag_view(request, tag_slug):
    tag = get_object_or_404(BlogTag, slug=tag_slug)
    posts = Blog.objects.filter(tag=tag)
    context = {
        'tag': tag,
        'posts': posts,
    }
    return render(request, 'components/post_list.html', context)

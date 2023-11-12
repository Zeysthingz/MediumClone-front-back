from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

import json

from .models import (
    Blog,
    BlogCategory,
    BlogTag,
    UserFavPost,
)
from .forms import BlogModelForm


@login_required(login_url='user_profile:login_view')
def create_blog_view(request):
    form = BlogModelForm()
    title = 'Create Blog'
    context = {
        'form': form,
        'title': title,
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

    return render(request, 'core/common_components/form.html', context)


@login_required(login_url='user_profile:login_view')
def post_edit_view(request, user_slug, post_slug):
    post = get_object_or_404(Blog, slug=post_slug)
    form = BlogModelForm(instance=post)
    title = 'Edit Blog'
    context = {
        'form': form,
        'title': title,
    }
    if request.user != post.user:
        messages.warning(request, 'You are not allowed to edit this post')
        return redirect('home_view')

    if request.method == 'POST':
        form = BlogModelForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            tags_data = json.loads(form.cleaned_data.get('tag'))
            for tag_data in tags_data:
                tag, created = BlogTag.objects.get_or_create(title=tag_data.get('value').lower())
                tag.is_active = True
                tag.save()
                f.tag.add(tag)
            messages.success(request, 'Blog edited successfully')
            return redirect('home_view')
    return render(request, 'core/common_components/form.html', context)


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


@login_required(login_url='user_profile:login_view')
def fav_update_view(request):
    if request.method == 'POST':
        post = get_object_or_404(Blog, slug=request.POST.get('slug'))
        print(post)
        if post:
            post_fav, created = UserFavPost.objects.get_or_create(
                user=request.user, post=post
            )
            if not created:
                post_fav.is_deleted = not post_fav.is_deleted
                post_fav.save()

        return JsonResponse({'status': '200'})

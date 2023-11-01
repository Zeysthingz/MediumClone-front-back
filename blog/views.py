from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

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

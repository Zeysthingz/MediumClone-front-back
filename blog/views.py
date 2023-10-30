from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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
            f.save()
            tags_data = json.loads(form.cleaned_data.get('tag'))
            print(type(tags_data))
            for tag_data in tags_data:
                print(tag_data)

                # tag_items, created = BlogTag.objects.get_or_create(title=item.item.get('value'))
                # # save to form
                # f.tag.add(tag_items)

    return render(request, 'create_blog.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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
            print(form.cleaned_data)
            print(form.cleaned_data.get('tag'))
            # f.save()

    return render(request, 'create_blog.html', context)

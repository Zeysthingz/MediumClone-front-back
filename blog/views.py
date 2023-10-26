from django.shortcuts import render
from .models import Blog, BlogCategory, BlogTag
from .forms import BlogModelForm


def create_blog_view(request):
    form = BlogModelForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        # to get media files we should add request.FILES or None
        form = BlogModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form)

    return render(request, 'create_blog.html', context)

from django.shortcuts import get_object_or_404, render
from blog.models import Blog
from user_profile.models import Profile


def all_post(request, user_slug):
    # We retrieve the posts of the user whose posts we want to read from the db.
    user = get_object_or_404(Profile, slug=user_slug)
    post = Blog.objects.filter(user=user)
    context = {
        'post': post,
    }
    return render(request, 'read/all_post.html', context)

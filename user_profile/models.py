from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=200)
    info = tinymce_models.HTMLField(blank=True, null=True)

    def __str__(self):
        return self.instagram

    def get_all_post_url(self):
        return reverse(
            'read:all_post',
            kwargs={
                "user_slug": self.slug,
            }
        )

    def get_edit_profile_url(self):
        return reverse(
            'user_profile:profile_edit_view',
        )

    def get_favorite_blog_url(self):
        return reverse(
            'user_profile:user_favorite_view',
        )

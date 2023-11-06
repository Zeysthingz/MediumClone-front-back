from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.instagram

    def get_absolute_url(self):
        return reverse(
            'read:all_post',
            kwargs={
                "user_slug": self.slug,
            }
        )

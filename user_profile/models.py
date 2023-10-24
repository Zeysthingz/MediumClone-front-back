from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.instagram

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Third Party Apps:
from autoslug import AutoSlugField
from tinymce import models as tinymce_models


class BaseModel(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('title',)


class BlogCategory(BaseModel):

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog:category_view',
            kwargs={
                "category_slug": self.slug
            }
        )


class BlogTag(BaseModel):
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog:tag_view',
            kwargs={
                "tag_slug": self.slug
            }
        )


class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(BlogTag)
    content = tinymce_models.HTMLField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='post/', blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'read:post_detail_view',
            kwargs={
                "user_slug": self.user.profile.slug,
                "post_slug": self.slug,
            }
        )

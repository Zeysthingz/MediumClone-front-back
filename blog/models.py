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


class BlogCategory(BaseModel):

    def __str__(self):
        return self.title

    # since we use a namspace whi adding todo third party app to core app, we should call view with this namespace.
    # we use this function to give html files to pah of view
    # def get_absolute_url(self):
    #     return reverse(
    #         'blog:category_view',
    #         kwargs={
    #             "category_slug": self.slug
    #         }
    #     )


class BlogTag(BaseModel):
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         'blog:tag_view',
    #         kwargs={
    #             "tag_slug": self.slug
    #         }
    #     )


class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(BlogTag)
    content = tinymce_models.HTMLField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='post/', blank=True, null=True)
    # to see how many people wiev the post
    viewer = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    # get absolute creates a path with the user friendly slug it takes from the url and also creates a path with the id.
    # The get_absolute_url method is responsible for constructing the URL for a
    # todo item. It uses the reverse function to generate the URL based on the provided view name and keyword arguments.
    # def get_absolute_url(self):
    #     return reverse(
    #         'blog:post_detail_view',
    #         kwargs={
    #             "category_slug": self.category.slug,
    #             "post_slug": self.slug,
    #         }
    #     )

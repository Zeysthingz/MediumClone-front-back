from django.contrib import admin
from .models import (
    Blog,
    BlogCategory,
    BlogTag,
)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    pass

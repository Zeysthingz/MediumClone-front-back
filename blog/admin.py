from django.contrib import admin
from .models import (
    Blog,
    BlogCategory,
    BlogTag,
)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'is_active', 'category', 'view_count']
    list_display_links = ['title', 'user', 'category', 'is_active', 'view_count']


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_display_links = ['title', 'is_active']


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_display_links = ['title', 'is_active']

from django.urls import path
from .views import (
    create_blog_view
)

# ın different app can be same url to avoid confusion
app_name = 'blog'
urlpatterns = [
    path('create/', create_blog_view, name='create_blog_view'),
]

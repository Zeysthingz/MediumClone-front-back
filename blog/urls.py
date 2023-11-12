from django.urls import path
from .views import (
    category_view,
    create_blog_view,
    fav_update_view,
    post_edit_view,
    tag_view,

)

# ın different app can be same url to avoid confusion
app_name = 'blog'
urlpatterns = [
    path('create/', create_blog_view, name='create_blog_view'),
    path('category/<slug:category_slug>/', category_view, name='category_view'),
    path('tag/<slug:tag_slug>/', tag_view, name='tag_view'),
    path('fav/update/', fav_update_view, name='fav_update_view'),
    path('<slug:user_slug>/<slug:post_slug>/edit/', post_edit_view, name='post_edit_view'),

]

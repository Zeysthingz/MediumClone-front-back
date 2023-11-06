from django.urls import path
from .views import (
    all_post,
    post_detail_view,

)

# ın different app can be same url to avoid confusion
app_name = 'read'
urlpatterns = [
    path('<slug:user_slug>/', all_post, name='all_post'),
    path('<slug:user_slug>/<slug:post_slug>/', post_detail_view, name='post_detail_view'),
]

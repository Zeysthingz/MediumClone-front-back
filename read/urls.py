from django.urls import path
from .views import (
    all_post
)

# ın different app can be same url to avoid confusion
app_name = 'read'
urlpatterns = [
    path('<slug:user_slug>/', all_post, name='all_post'),
]

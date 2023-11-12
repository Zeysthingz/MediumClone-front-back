from django.urls import path
from .views import (
    login_view,
    logout_view,
    user_favorite_view,
    profile_edit_view,
    register_view,
)

# ın different app can be same url to avoid confusion
app_name = 'user_profile'
urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),

    # Register page
    path('register/', register_view, name='register_view'),

    # Profile edit page
    path('profile/edit/', profile_edit_view, name='profile_edit_view'),

    # User's favorite blogs page

    path('user/favs/', user_favorite_view, name='user_favorite_view'),

]

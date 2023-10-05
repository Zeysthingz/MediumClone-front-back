from django.urls import path
from .views import login_view

# ın different app can be same url to avoid confusion
app_name = 'user_profile'
urlpatterns = [
    path('login/', login_view, name='login_view')
    ,
]

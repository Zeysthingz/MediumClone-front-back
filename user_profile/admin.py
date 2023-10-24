from django.contrib import admin
from .models import Profile


# register app to admin panel with decorator
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

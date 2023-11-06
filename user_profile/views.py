from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Profile
from slugify import slugify


# login page
def login_view(request):
    context = {

    }
    # TODO: if user is already logged in should be redirect to home page

    if request.user.is_authenticated:
        messages.info(request, "Dear" "  "   f'{request.user.username}    You already logged in.')
        return redirect('home_view')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(email) < 6 or len(password) < 1:
            messages.warning(request, "Please enter valid email and password")
            # redirects to login page
            return redirect('user_profile:login_view')

        # authenticate takes username as default but we can change it to email
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username} Successfully logged in.')
            return redirect('home_view')

    return render(request, 'login.html', context)


def logout_view(request):
    # message should be added before logout function after logout function we are not able to have user info
    messages.info(request, f'{request.user.username} Successfully logged out.')
    logout(request)
    return redirect('home_view')


# register page
def register_view(request):
    context = {

    }
    if request.method == "POST":
        post_info = request.POST
        first_name = post_info.get('first_name')
        last_name = post_info.get('last_name')
        email = post_info.get('email')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        instagram_account = post_info.get('instagram_account')

        if len(first_name) < 2 or len(last_name) < 2 or len(email) < 2 or len(password) < 2:
            messages.warning(request, "Please enter valid information. Informations can not be less than two characters"
                             )
            return redirect('user_profile:register_view')
        if password != password_confirm:
            messages.warning(request, "Please enter same password")
            return redirect('user_profile:register_view')
        user, created = User.objects.get_or_create(username=email, email=email)
        # if user is not created that mens user already exists in database
        if not created:
            user_login = authenticate(request, email=email, password=password)
            if user is not None:
                messages.warning(request, "This email is already exists... Redirecting to home page")
                # if we can authenticate user we logged in user
                login(request, user_login)
                return redirect('home_view')
            messages.warning(request, "User already exists but can't login... Redirecting to login page")
            return redirect('user_profile:login_view')
        # if user is not in database already we create user and register it
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)

        profile, profile_created = Profile.objects.get_or_create(user=user)
        profile.instagram = instagram_account
        profile.slug = slugify(f"{first_name}-{last_name}")
        user.save()
        profile.save()

        messages.success(request, f'{user.first_name} Succesfully registered ..')
        user_login = authenticate(request, email=email, password=password)
        login(request, user_login)
        return redirect('home_view')

    return render(request, 'register.html', context)

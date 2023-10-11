from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def login_view(request):
    context = {

    }
    # TODO: if user is already logged in should be redirect to home page

    if request.user.is_authenticated:
        # TODO give info as you already logged in
        messages.info(request, "Dear" "  "   f'{request.user.username}    You already logged in.')
        return redirect('home_view')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(email) < 6 or len(password) < 6:
            messages.warning(request, "Please enter valid email and password")
            # redirects to login page
            return redirect('user_profile:login_view')

        user = authenticate(request, email=email, password=password)
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
        profile_info = request.POST
        first_name = profile_info.get('first_name')
        last_name = profile_info.get('last_name')
        email = profile_info.get('email')
        password = profile_info.get('password')
        password_confirm = profile_info.get('password_confirm')
        # instagram_account = profile_info.get('instagram_account')
        if len(first_name) < 2 or len(last_name) < 2 or len(email) < 2 or len(password) < 2:
            messages.warning(request,
                             "Please enter valid information. Informations can not be less than two characters"
                             )
        if password != password_confirm:
            messages.warning(request, "Please enter same password")
            return redirect('user_profile:register_view')
        user, created = User.objects.get_or_create(email=email)
        # if user is not created that mens user already exists in database
        if not created:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                messages.warning(request, "This email is already exists... Redirecting to home page")
                # if we can authenticate user we logged in user
                login(request, user)
                return redirect('home_view')
            messages.warning(request, "User already exists but can't login... Redirecting to login page")
            return redirect('user_profile:login_view')
    return render(request, 'register.html', context)

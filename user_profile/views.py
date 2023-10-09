from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect


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

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username} Successfully logged in.')
            return redirect('home_view')
        # else:
        #     messages.warning(request, "Please enter valid email and password.")
        #     return redirect('user_profile:login_view')
    return render(request, 'login.html', context)


def logout_view(request):
    # message should be added before logout function after logout function we are not able to have user info
    messages.info(request, f'{request.user.username} Successfully logged out.')
    logout(request)
    return redirect('home_view')


def register_view(request):
    context = {

    }
    if request.method == "POST":
        print(request.POST)
    return render(request, 'register.html', context)

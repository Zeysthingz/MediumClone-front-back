from django.contrib.auth import authenticate, login
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
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username} Successfully logged in.')
            return redirect('home_view')
        # else:
        #     messages.warning(request, "Please enter valid email and password.")
        #     return redirect('user_profile:login_view')
    return render(request, 'login.html', context)

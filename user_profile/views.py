from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect


def login_view(request):
    context = {

    }
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"username: {email} password: {password}")
        user = authenticate(request, username=email, password=password)
        # TODO: info user abt logged in
        # TODO: validate fields are correct or not
        if user is not None:

            login(request, user)
            # you can directly redirect to view
            return redirect('home_view')
    return render(request, 'login.html', context)

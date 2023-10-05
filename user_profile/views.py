from django.shortcuts import render


def login_view(request):
    # if user authenticated direct to  home page
    if request.user.is_authenticated:
        return render(request, 'base.html')
    return render(request, 'login.html')

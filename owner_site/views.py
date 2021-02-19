from django.shortcuts import render


def owner_index(request):
    test = 'test'
    context = {'test': test}
    return render(request, 'owner.html', context)


def owner_login(request):
    test = 'login'
    context = {'test': test}
    return render(request, 'owner_login.html', context)


def owner_signup(request):
    test = 'signup'
    context = {'test': test}
    return render(request, 'owner_signup.html', context)

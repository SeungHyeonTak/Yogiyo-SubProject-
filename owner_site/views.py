from django.shortcuts import render


def index(request):
    test = 'test'
    context = {'test': test}
    return render(request, 'base.html', context)

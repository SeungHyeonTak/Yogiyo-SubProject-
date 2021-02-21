from django.shortcuts import render


def process(request):
    context = {}
    return render(request, 'join/process.html', context)

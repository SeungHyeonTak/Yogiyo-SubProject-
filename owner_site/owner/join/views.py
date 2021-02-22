from django.shortcuts import render


def process(request):
    context = {}
    return render(request, 'join/process.html', context)


def online_entry(request):
    context = {}
    return render(request, 'join/request.html', context)

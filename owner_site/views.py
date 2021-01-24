from django.shortcuts import render


def owner_index(request):
    test = 'test'
    context = {'test': test}
    return render(request, 'owner.html', context)

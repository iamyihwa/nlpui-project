from django.shortcuts import render


def learnmore(request):
    return render(request, 'learnmore.html')

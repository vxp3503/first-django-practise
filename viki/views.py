from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    tiki = request.POST.get('text', 'default')
    riki = request.POST.get('back', 'default')

    analyzed = tiki
    niki = {'purpose': 'Remove', 'analyzed_text': analyzed}
    if riki == "on":
        return render(request, 'analyze.html', niki)
    else:
        return HttpResponse("error")
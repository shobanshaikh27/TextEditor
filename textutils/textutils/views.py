# created by me
from email.policy import default
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    caps = request.POST.get('caps', 'off')
    lineremover = request.POST.get('lineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    analyzed = ""
    if djtext == "" and analyzed == "":
        params = {'purpose': 'Enter some texts in text area'}
        djtext = analyzed
        return render(request, 'analyze.html', params)

    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for x in djtext:
            if x not in punctuations:
                analyzed = analyzed + x
        params = {'purpose': 'Removes Punctuations', 'Analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if (caps == "on"):
        analyzed = ""
        for x in djtext:
            analyzed = analyzed + x.upper()
        params = {'purpose': 'Capitalize letters', 'Analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if (lineremover == "on"):
        analyzed = ""
        for x in djtext:
            if x != '\n' and x != '\r':
                analyzed = analyzed + x
        params = {'purpose': 'Line Remover', 'Analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if (spaceremover == "on"):
        analyzed = ""
        for index, x in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + x
        params = {'purpose': 'Line Remover', 'Analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if (charcount == "on"):
        analyzed = ""
        count = 0
        for index, x in enumerate(djtext):
            if djtext[index] == " ":
                pass
            else:
                count = count + 1
        params = {'purpose': 'Character Counter',
                  'counter': {'Total number of Words are': count}}
        return render(request, 'analyze.html', params)
    if (removepunc != 'on' and caps != "on" and lineremover != "on" and spaceremover != "on" and charcount != "on"):
        return HttpResponse('<div class="container-sm mt-4"><h1>Error!!!</h1><br><h3>You should select at least one option(Toggle Bar)</h3></div>')

    return render(request, 'analyze.html', params)

from django.http import HttpResponse
from django.shortcuts import render

import operator


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET["fulltext"]
    words = fulltext.split()

    wordlist = {}

    for word in words:
        if word in wordlist:
            wordlist[word] += 1
        else:
            wordlist[word] = 1

    sortedword = sorted(wordlist.items(), key= operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {"fulltext": fulltext, "wordcount": len(words), "wordlist": sortedword})

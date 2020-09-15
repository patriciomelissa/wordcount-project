from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist= fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increase the value
            worddictionary[word] += 1
        else:
            #add number
            worddictionary[word] = 1

    sortedlist = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'wordlist':len(wordlist), 'sortedlist':sortedlist})

from django.shortcuts import render
import operator
# Create your views here.


def home(request):
    return render(request, 'count/home.html', {})


def counted(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
        
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
                #increase
                worddictionary[word] += 1
        else:
        #add to dictionary
           worddictionary[word] = 1
           
    sortWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True' )
 
    return render(request, 'count/counted.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddictionary': worddictionary.items})


def about(request):
    return render(request, 'count/about.html', {about: 'about'})

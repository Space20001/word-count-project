from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'count/home.html', {})


def counted(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    for word in wordlist:
        
        worddictionary

        for word in wordlist:
            if word in worddictionary:
                #increase
                worddictionary[word] += 1

                else
                #add to dictionary
                worddictionary[word] = 1

    return render(request, 'count/counted.html', {'fulltext': fulltext, 'count': len(wordlist)})


def about(request):
    return render(request, 'count/about.html', {about: 'about'})

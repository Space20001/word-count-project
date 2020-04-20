from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'count/home.html', {})


def counted(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    return render(request, 'count/counted.html', {'fulltext': fulltext})
    fulltext

    
def about(request):
    return render(request, 'count/about.html', {about: 'about'})

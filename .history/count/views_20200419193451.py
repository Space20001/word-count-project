from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'count/home.html', {})


def counted(request):
    request.GET
    return render(request, 'count/counted.html', {})

    
def about(request):
    return render(request, 'count/about.html', {about: 'about'})

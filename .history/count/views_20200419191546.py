from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'count/home.html', {})


def counted(request):
    return render(request, 'count/count.html', {})

    
def about(request):
    return render(request, 'count/about.html', {about: 'about'})

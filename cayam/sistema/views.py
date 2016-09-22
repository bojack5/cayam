from django.shortcuts import render


def index(request):
    return render(request , 'sistema/index.html', {})

# Create your views here.

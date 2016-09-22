from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.core.urlresolvers import reverse


def review(request):
    if request.user.is_authenticated():
        print('Autenicado')
        return HttpResponseRedirect('/sistema/')
    else:
        print('Entrele pues')
        return index(request)

            
    

def index(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        print(usuario,password)
        user = authenticate(username = usuario , password = password)

        if user:
            if user.is_active:
                login(request , user)
                print('entro por reverse')
                return HttpResponseRedirect('/sistema/')
            else:
                
                return HttpResponse('Tu cuenta ha sido desabilitada')
        else:
            print("Invalid login details: {0}, {1}".format(usuario, password))
            return HttpResponse("Datos erroneos")

    else:
        print('entro por ultimo') 
           
        
        return render(request , 'login/index.html',{})
    

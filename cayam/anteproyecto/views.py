from django.shortcuts import render
from anteproyecto.forms import AnteproyectoForm , PartidaForm , PpreguntaForm ,ApreguntaForm


def formularios_view(request):

    form = ApreguntaForm()    
    form2 = PpreguntaForm()

    if request.method == 'POST':
        if request.POST.get('tipo','') == 'Partida':

            form = PartidaForm()

            return render(request,'anteproyecto/index.html',{
            	                                            'submit': 'Agregar Partida',
            	                                            'titulo' : 'Cayam | Partida' ,
            	                                            'subtitulo' : 'Alta de Partida',
            	                                            'form' : form})

        if request.POST.get('tipo','') == 'Anteproyecto':

            form = AnteproyectoForm()

            return render(request,'anteproyecto/index.html',{
            	                                            'titulo' : 'Cayam | Anteproyecto',
            	                                            'subtitulo' : 'Alta de Anteproyecto',
            	                                            'form' : form,
            	                                            'submit':'Agregar Proyecto',
            	                                            })  

        if request.POST.get('tipo','') == 'PartidaProceso':

            form = PartidaForm(request.POST)
            
             
            if form.is_valid():
                form.save(commit = True)



                return render(request,'anteproyecto/index.html',{'titulo' : 'Cayam | Partida',
                	                                            'subtitulo' : 'Exito!',
                	                                            'texto_gracias' : 'Se dio de Alta Exitosamente la partida!'})
            else:
                return render(request , 'anteproyecto/index.html',{
                                                                   'titulo':'Error',
                                                                   'subtitulo' : 'Errores encontrados',
                                                                   'form':form,
                                                                   'submit' : 'Alta de Partida',



                                                                   })
                


        if request.POST.get('tipo','') == 'AnteproyectoProceso':

            form = AnteproyectoForm(request.POST)

            if form.is_valid():
                form.save(commit = True)

                return render(request,'anteproyecto/index.html',{'titulo' : 'Cayam | Anteproyecto',
                	                                            'subtitulo' : 'Exito',
                	                                            'texto_gracias' : 'Se dio de Alta Exitosamente el Anteproyecto!'})            
        
            else:
                return render(request , 'anteproyecto/index.html',{
                                                                   'titulo':'Error',
                                                                   'subtitulo' : 'Errores encontrados',
                                                                   'form':form,
                                                                   'submit' : 'Alta de Partida',



                                                                   })
    
    

    return render(request , 'anteproyecto/index.html' , {'titulo' : 'Cayam | Escoge',
        	                                            'subtitulo': 'Selecciona uno...' ,
        	                                            'form' : form,
        	                                            'form2':form2,
        	                                            'submit': 'Anteproyecto',
        	                                            'submit2': 'Partida',
        	                                            }) 

# Create your views here.

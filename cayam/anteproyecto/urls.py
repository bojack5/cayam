from django.conf.urls import url
from django.contrib import admin
#from django.conf.urls import include
from anteproyecto import views


urlpatterns = [
    url(r'^$', views.formularios_view , name = 'anteproyecto_index'),
    

    
]

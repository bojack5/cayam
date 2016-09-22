from django.conf.urls import url
from django.contrib import admin
#from django.conf.urls import include
from sistema import views


urlpatterns = [
    url(r'^$', views.index , name = 'sistema_index'),
    

    
]

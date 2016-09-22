from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from login import views
#from sistema import views


urlpatterns = [
    url(r'^$', views.review , name = 'login_index'),
    


    
]

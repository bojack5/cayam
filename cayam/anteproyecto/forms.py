#!/usr/bin/env python3

from django import forms
from django.contrib.auth.models import User
from anteproyecto.models import Partida , Anteproyecto
from datetime import datetime

class PartidaForm(forms.ModelForm):
    tipo   = forms.CharField(widget = forms.HiddenInput() , required = False ,initial = 'PartidaProceso')
    
   
    class Meta:
        model = Partida
        exclude = ('total',)
        error_messages = {
            'nombre': {
                'required': ("This writer's name is too long."),
            }}


class AnteproyectoForm(forms.ModelForm):
    tipo   = forms.CharField(widget = forms.HiddenInput() , required = False ,initial = 'AnteproyectoProceso')
    class Meta:
        model = Anteproyecto
        fields = ('nombre','descripcion','principal','secundario','impacto_del_proyecto',)
        error_messages = {
            'nombre': {
                'required': ("Introduce Nombre del proyecto."),
            },
            'descripcion': {
                'required': ("Descripcion requerida."),
            },
            'principal': {
                'required': ("selecciona una o mas Partidas manteniendo presionado la tecla cntrl."),
            },
            'secundario': {
                'required': ("selecciona una o mas Partidas manteniendo presionado la tecla cntrl."),
            },
            'impacto_del_proyecto': {
                'required': ("Este campo es requerido."),
            },
            }

class ApreguntaForm(forms.Form):
    tipo   = forms.CharField(widget = forms.HiddenInput() , required = False ,initial = 'Anteproyecto')
    
class PpreguntaForm(forms.Form):
    tipo   = forms.CharField(widget = forms.HiddenInput() , required = False ,initial = 'Partida')
    

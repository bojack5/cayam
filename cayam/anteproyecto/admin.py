from django.contrib import admin
from anteproyecto.models import Anteproyecto , Partida

class AnteproyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    filter_horizontal = ('principal','secundario')
    class Meta:
        verbose_name_plural = 'Anteproyectos'
    def __str__(self):
        return self.nombre    

class PartidaAdmin(admin.ModelAdmin):    
    list_display = ('cantidad' , 'descripcion' , 'importe' , 'total')

    class Meta:
        verbose_name_plural = 'Partidas'

    def __str__(self):
        return self.descripcion

admin.site.register(Anteproyecto,AnteproyectoAdmin)
admin.site.register(Partida)

# Register your models here.

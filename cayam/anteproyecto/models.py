from django.db import models

class Partida(models.Model):
    cantidad    = models.IntegerField(default = 1)
    descripcion = models.CharField(max_length = 100)
    importe     = models.FloatField()
    

    def __str__(self):
    	return '%s - importe %s | total : %s'%(self.descripcion , 
    		                                   self.importe,
    		                                   self.importe * self.cantidad)
    
class Anteproyecto(models.Model):
    nombre      = models.CharField(max_length = 140)
    descripcion = models.TextField()
    principal   = models.ManyToManyField('Partida', related_name = 'PartidaP')
    secundario  = models.ManyToManyField('Partida', related_name = 'PartidaS')
    impacto_del_proyecto = models.CharField(max_length= 140)

    def __str__(self):
        return self.nombre

# Create your models here.

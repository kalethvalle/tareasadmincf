from django.db import models

# Create your models here.
class TaskManager(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescrip = models.TextField()
    taskEnd = models.BooleanField(default=False)
    taskFile = models.FileField(upload_to='static/%Y/%m/%d/', blank=True, null=True)
    taskResol = models.BooleanField(default=False)
    taskFechaCrea = models.DateField()

    def save(self, *args, **kwargs):
        self.taskTitle = self.taskTitle.upper()
        super(TaskManager, self).save()

        if self.taskResol:
           from .test import _testInicio
           _testInicio(self.id)

class Prefijo(models.Model):
    id_task = models.IntegerField()
    prefijo = models.CharField(max_length=6)
    fecha_ini_pref = models.DateField()
    vigencia_pref = models.IntegerField()
    nro_ini_pref = models.IntegerField()
    nro_fin_pref = models.IntegerField()
    resolucion_pref = models.IntegerField()
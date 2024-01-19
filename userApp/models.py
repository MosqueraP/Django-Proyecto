from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    firs_name = models.CharField(max_length=30, verbose_name='Nombre')
    lasts_name = models.CharField(max_length=30, verbose_name='Apellido')
    cars = models.ManyToManyField('Car', verbose_name='Carros del usuario')

    def __str__(self):
        return self.firs_name 

STATUS_CHOISES = (
		('R', 'Reviewd'),
		('N', 'Not Reviewd'),
		('E', 'Error'),
		('A', 'Accepted'),
)
class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    reting = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOISES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    #Fue lanzado la ultima semana
    def was_released_last_week(self):
        if self.release_date < datetime(2023,6,6):
            return 'lanzamiento antes de la semana pasada'
        else:
            return 'lanzamiento esta semana'
        
    @property
    def get_full_name(self):
        return f'Estes el nombre completo del sitio web: {self.ame}'

    def __str__(self):
        return self.name
    
    #busqueda de sitio por su ID
    def get_absolute_url(self):
        return f'/website/{self.id}'
    
    # sobre escribiendo metodo save
    def save(self, *args, **kwargs):
        print('Estamos guardando')
        super().save( *args, **kwargs)

    class Meta:
        ordering = ['reting']
        db_table = 'Nombre de la tabla'
        verbose_name = 'sitio Web'
        verbose_name_plural = 'sitio Webs'


class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)

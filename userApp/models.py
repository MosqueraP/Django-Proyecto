from django.db import models

# Create your models here.
class User(models.Model):
    firs_name = models.CharField(max_length=30, verbose_name='Nombre' )
    lasts_name = models.CharField(max_length=30, verbose_name='Apellido' )  

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


class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)

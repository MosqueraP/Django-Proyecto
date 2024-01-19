from django.db import models

# Create your models here.
class User(models.Model):
    firs_name = models.CharField(max_length=30, verbose_name='Nombre' )
    lasts_name = models.CharField(max_length=30, verbose_name='Apellido' )  

    def __str__(self):
        return self.firs_name 

# STATUS_CHOISES = (
# 		('R', 'Reviewd'),
# 		('N', 'Not Reviewd'),
# 		('E', 'Error'),
# 		('A', 'Acepted'),
# )
class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    release_date = models.DateField()
    reting = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
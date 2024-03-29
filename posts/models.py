from django.db import models
from django.shortcuts import redirect
# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length = 100)
    tangline = models.TextField()
    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=250)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name='entries')
    n_comments = models.IntegerField()
    n_pingbancks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
    

    def get_absolute_url(self):
        return redirect(reversed('entries:entry-detail', kwargs={'id':self.id}))
    
    


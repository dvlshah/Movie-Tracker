from django.db import models
from django.core.validators import URLValidator


class Movies(models.Model):

    class Meta:
        verbose_name_plural = 'Movies'

    name = models.CharField(max_length=50,blank=True)
    cover_image_url = models.TextField(validators=[URLValidator()],null=True)
    release_date = models.DateField(null=True)
    genre = models.CharField(max_length=50,blank=True)
    lead_actors = models.ManyToManyField('Actor')
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Actor(models.Model):

    class Meta:
        verbose_name_plural = 'Actor'
        ordering = ('name',)

    #movies = models.ManyToManyField('Movies')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Director(models.Model):

    class Meta:
        verbose_name_plural = 'Director'

    #movies = models.ForeignKey('Movies', on_delete=models.CASCADE,default=1,null=False)
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name

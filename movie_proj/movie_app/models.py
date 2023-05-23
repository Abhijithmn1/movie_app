from django.db import models


# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=200)
    disc = models.TextField()
    year = models.IntegerField()
    poster = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

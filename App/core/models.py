from django.db import models

# Create your models here.

class Image(models.Model):

    path = models.ImageField(upload_to = 'temp')


    def __str__(self):
        return str(self.id)
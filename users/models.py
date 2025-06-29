from django.db import models

# Create your models here.
class Appuser(models.Model):
    picture = models.URLField(max_length=200)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    count_post = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.id}{self.username}" # pylint: disable=no-member

class Administrator(models.Model):
    picture = models.URLField(max_length=200)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    position = models.CharField( max_length=50)
    
    def __str__(self):
        return f"{self.id}{self.username}" # pylint: disable=no-member
    

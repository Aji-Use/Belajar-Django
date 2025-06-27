from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=255)
    linkImg = models.URLField(default='https://example.com/default.jpg')
    body = models.TextField()
    receipes = models.TextField(default='write a receipe')
    category = models.CharField(max_length=255)
    dateTime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False)
    
    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()
    
    def __str__(self):
        return f"{self.id} {self.title}" # pylint: disable=no-member
    

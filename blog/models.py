from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=255)
    linkImg = models.URLField()
    body = models.TextField()
    receipes = models.TextField()
    category = models.CharField(max_length=255)
    dateTime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.category = self.category.lower()
        super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.id} {self.title}" # pylint: disable=no-member
    

from django.db import models

# Create your models here.

class NewBlog(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=250)
    content = models.TextField()
    author = models.CharField(max_length=225)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='sample.png', blank=True)

    def __str__(self):
        return f'{self.title}'
    
    

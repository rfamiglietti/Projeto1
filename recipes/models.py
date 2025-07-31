from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    intrucions = models.TextField()
    cooking_time = models.ImageField(help_text='in minutes')
    
    def __str__(self):
        return self.title
# Create your models here.

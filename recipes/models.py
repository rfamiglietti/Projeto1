from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text='in minutes')
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Recipes'
    
    def __str__(self):
        return self.title
   
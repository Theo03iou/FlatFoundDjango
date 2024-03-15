from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name # Shows the name of property on admin page

class Property(models.Model):
    category = models.ForeignKey(
        Category, related_name='properties', on_delete=models.CASCADE)
    price_pcm = models.FloatField()
    address = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='prop_images', blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE) # If the user is deleted then so are their properties.
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
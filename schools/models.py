from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return '%s' % self.name
    
    class Meta:
        ordering = ['id']
from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=50)
    created_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_date','id']
    
    def __str__(self):
        return self.name

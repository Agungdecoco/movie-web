from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img_path = models.CharField(max_length=255)  
    duration = models.IntegerField()  
    genre = models.JSONField() 
    language = models.CharField(max_length=50)
    mpaa_rating_type = models.CharField(max_length=10)
    mpaa_rating_label = models.CharField(max_length=255)
    user_rating = models.IntegerField()

    def __str__(self):
        return self.name

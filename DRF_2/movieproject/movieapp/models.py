from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=50)
    director=models.CharField(max_length=50)
    release_date=models.DateTimeField(auto_now_add=True)
    genre=models.CharField(max_length=20)

    def __str__(self):
        return self.title
from django.db import models
    
class Hero(models.Model):
    heroName=models.CharField(max_length=200)
    popularity=models.IntegerField()

    def __str__(self):
        return self.heroName
    
class Movie(models.Model):
    movieName=models.CharField(max_length=200)
    rating=models.IntegerField()
    hero=models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.movieName
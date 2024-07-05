from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    published_date=models.DateField()
    ISBN=models.CharField(max_length=13, unique=True)
    pages=models.IntegerField()
    cover=models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title
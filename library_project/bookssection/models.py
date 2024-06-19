from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publication_date=models.DateField()
    isbn=models.CharField(max_length=13, unique=True)
    pages=models.IntegerField()
    cover=models.URLField(blank=True, null=True)
    language=models.CharField(max_length=50, default="English")

    def __str__(self):
        return self.title
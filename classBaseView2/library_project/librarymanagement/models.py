from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=40)
    dob=models.DateField()

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    published_date=models.DateField()
    ISBN=models.CharField(max_length=13, unique=True)
    pages=models.IntegerField()
    cover=models.URLField(null=True)
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self) -> str:
        return self.title
from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=250)
    publicationDate=models.DateField()

    def __str__(self):
        return self.title
    
class Author(models.Model):
    name=models.CharField(max_length=250)
    dateOfBirth=models.DateField()
    book=models.ManyToManyField(Book, related_name="authors")

    def __str__(self):
        return self.name
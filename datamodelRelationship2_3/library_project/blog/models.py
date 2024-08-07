from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
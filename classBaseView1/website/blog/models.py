from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    comment=models.CharField(max_length=200)
    post=models.ManyToManyField(Post, related_name="comments")

    def __str__(self) -> str:
        return self.comment
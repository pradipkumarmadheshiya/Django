from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
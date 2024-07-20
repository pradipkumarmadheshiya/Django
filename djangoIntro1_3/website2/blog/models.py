from django.db import models

# Create your models here.
# {"postId":1, "title":"first list", "content":"This is the first list of blog"}

class posts(models.Model):
    postId=models.IntegerField()
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=200)

    def __str__(self):
        return self.title
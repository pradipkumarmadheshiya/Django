from django.db import models

class ReviewModel(models.Model):
    username=models.CharField(max_length=50)

    
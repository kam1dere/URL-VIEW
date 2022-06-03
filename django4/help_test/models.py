from django.db import models

class Blog(models.Model):
    name=models.CharField(max_length=200)
    tags = models.TextField()

    def __str__(self):
        return self.name
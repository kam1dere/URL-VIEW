from django.db import models


class Statya(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name
# Create your models here.

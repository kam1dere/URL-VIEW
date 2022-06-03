from django.db import models


class Nitik(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    kolvo = models.PositiveIntegerField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('myns:absdetail', kwargs={'pk': self.pk, 'slug': self.slug})




# Create your models here.

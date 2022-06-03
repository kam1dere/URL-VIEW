from django.db import models
from django.urls import reverse


class Page(models.Model):
    class Meta:
        verbose_name = 'Страница id, slug, namespace'
        verbose_name_plural = 'Страницы id, slug, namespace'

    name = models.CharField(max_length=160, verbose_name='Напишите заголовок',
                            help_text='Максимум 160 символов')
    content = models.TextField(blank=True, verbose_name='Напишите контент')
    slug = models.SlugField(unique=True, verbose_name='Слаг',
                            db_index=True)
    data_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    data_updated = models.DateTimeField(auto_now=True, verbose_name='Дата правки')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('yesNS:detail_get', kwargs={'pk': self.pk, 'slug': self.slug})

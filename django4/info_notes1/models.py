from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=80, verbose_name='имя сайта',
                            help_text='Не более 80 символов', unique=True)
    website = models.URLField(verbose_name='Сайт', blank=True, unique=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    slug = models.SlugField(max_length=80, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Название сайта'
        verbose_name_plural = 'Название сайтов'


class Nick(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    personal_website = models.URLField(default='Нет сайта', blank=True)
    picture = models.ImageField(upload_to='info_notes_picture/', null=True, default='nick.png')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Имя или ник автора"
        verbose_name_plural = "Имена или ники авторов"


class Note(models.Model):
    class Meta:
        verbose_name = "Контент"
        verbose_name_plural = "Контент"

    title = models.CharField(max_length=120, unique=True)
    nick = models.ManyToManyField(Nick)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    data_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.title

# Create your models here.

# Create your models here.

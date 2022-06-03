# Generated by Django 4.0.4 on 2022-05-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160)),
                ('content', models.TextField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('data_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

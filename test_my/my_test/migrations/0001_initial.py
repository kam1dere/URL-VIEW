# Generated by Django 4.0 on 2022-05-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nitik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True)),
                ('kolvo', models.PositiveIntegerField(blank=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]

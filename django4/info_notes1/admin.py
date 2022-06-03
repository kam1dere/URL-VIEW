from django.contrib import admin
from .models import Site, Nick, Note


@admin.register(Site)
class SitesAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'date_added']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Nick)
class NickAdmin(admin.ModelAdmin):
    list_display = ['name', 'personal_website', 'picture']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Note)
class NickAdmin(admin.ModelAdmin):
    list_display = ['title', 'data_created']
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.

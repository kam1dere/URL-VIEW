from django.contrib import admin

from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'data_created', 'data_updated']
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.

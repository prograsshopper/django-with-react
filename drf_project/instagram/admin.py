from django.contrib import admin

from .models import Post


@admin.register
class PostAdmin(admin.ModelAdmin):
    search_fields = ['message']
    list_display = ['pk', 'message', 'author']


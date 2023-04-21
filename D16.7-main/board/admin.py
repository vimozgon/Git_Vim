from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author', 'time_public']
    list_filter = ('author', 'time_public')


admin.site.register(Post, PostAdmin)

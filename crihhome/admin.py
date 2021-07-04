from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline')
admin.site.register(Post, PostAdmin)

admin.site.register(Category)


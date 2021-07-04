from django.contrib import admin
from .models import Course, Category


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
admin.site.register(Course, CourseAdmin)

admin.site.register(Category)
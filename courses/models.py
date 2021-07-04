from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, blank='', editable=False)

    def __str__(self):
        return self.title

    def get_category_url(self):
        kwargs = {
            'slug' : self.slug,
        }
        return reverse('', Kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-updated']


class Course(models.Model):
    STATUS_CHOICES = (
        ('Published', 'Published'),
        ('Draft', 'Draft')
    )
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='post_image', default='images1.jpg')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    author = models.CharField(max_length=100, default='Best Selling Author')
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, blank='', editable=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='Draft')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk:': self.id,
            'slug': self.slug,
        }
        return reverse('', Kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-updated']





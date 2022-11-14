from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Blog(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(default='Add some content here')
    publication_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django.views.generic import *

from blog.models import *


class BlogView(ListView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = 'blog/blog_main.html'
    context_object_name = 'blog'


class CategoryView(ListView):
    model = Category
    template_name = 'blog/blog_main.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'])


class PostView(DetailView):
    model = Blog

from django.urls import path

from blog.views import *

urlpatterns = [
    path('home/', BlogView.as_view(), name='blog'),
    path('home/<slug:category_slug>', CategoryView.as_view(), name='categories'),
    path('home/<slug:category_slug>/<int:post_id>', PostView.as_view(), name='post')
]

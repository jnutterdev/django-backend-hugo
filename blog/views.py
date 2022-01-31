from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'
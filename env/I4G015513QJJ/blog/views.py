from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post 

class PostListview(CreateView):
    model = Post 

# Create your views here.

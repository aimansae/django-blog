from django.shortcuts import render
from django.views import generic #library
from .models import Post
#in VIEWS:
# create code
# create template to render
# connect URL in urls.py
# #classes to resuse code 
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
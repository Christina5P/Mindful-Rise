from django.shortcuts import render, get_object_or_404
from django.urls import path, include
from django.urls import reverse

# Create your views here.

class PostList(generic.ListView):
    """
    A view to list all posts with status 'published'.
    Generic ListView is a standard view
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def blog_index(request):
    """
    Display all blog posts ordered by creation date in descending order.
    Render from index.html
    """
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
